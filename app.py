from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        characters = string.ascii_lowercase  # Default to lowercase if nothing selected
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        view = request.form.get('view', 'generate')
        
        if view == 'generate':
            length = int(request.form.get('length', 12))
            use_lowercase = 'lowercase' in request.form
            use_uppercase = 'uppercase' in request.form
            use_numbers = 'numbers' in request.form
            use_symbols = 'symbols' in request.form
            
            password = generate_password(
                length, 
                use_lowercase, 
                use_uppercase, 
                use_numbers, 
                use_symbols
            )
            return jsonify({'password': password})
            
        elif view == 'check':
            password = request.form.get('password')
            score = 0
            feedback = []
            
            # Vérification de la longueur
            if len(password) >= 12:
                score += 2
            elif len(password) >= 8:
                score += 1
                feedback.append("Un mot de passe plus long serait plus sécurisé")
            else:
                feedback.append("Le mot de passe doit contenir au moins 8 caractères")
            
            # Vérification des caractères
            if any(c.isupper() for c in password):
                score += 1
            else:
                feedback.append("Ajoutez des lettres majuscules")
                
            if any(c.islower() for c in password):
                score += 1
            else:
                feedback.append("Ajoutez des lettres minuscules")
                
            if any(c.isdigit() for c in password):
                score += 1
            else:
                feedback.append("Ajoutez des chiffres")
                
            if any(not c.isalnum() for c in password):
                score += 1
            else:
                feedback.append("Ajoutez des caractères spéciaux")

            # Détermination de la force
            if score >= 5:
                strength = "Très fort"
                color = "#007E33"
            elif score == 4:
                strength = "Fort"
                color = "#00c851"
            elif score == 3:
                strength = "Moyen"
                color = "#ffdb4a"
            elif score == 2:
                strength = "Faible"
                color = "#ffa700"
            else:
                strength = "Très faible"
                color = "#ff4444"

            return jsonify({
                'strength': strength,
                'color': color,
                'feedback': feedback
            })
    
    # Pour les requêtes GET
    view = request.args.get('view', 'generate')
    return render_template('index.html', view=view)

if __name__ == '__main__':
    app.run(debug=True) 