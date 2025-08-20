from flask import Flask, render_template, request

app = Flask(__name__)

disease_data = {
    "الحمى": {
        "keywords": ["حمى", "حرارة", "سخونة", "ارتفاع الحرارة", "تعرق", "قشعريرة"],
        "advice": "اشرب الكثير من السوائل، وارتَح، وإذا استمرت الحرارة أكثر من 3 أيام راجع الطبيب. يمكن استخدام باراسيتامول (Paracetamol) لتخفيض الحرارة."
    },
    "نزلة برد": {
        "keywords": ["زكام", "رشح", "انسداد الأنف", "عطس", "كحة", "احتقان الحلق"],
        "advice": "تناول سوائل دافئة واسترح. يمكن استخدام مضادات الاحتقان مثل الأوكسي ميترولين بخاخ الأنف ومسكنات الألم مثل الإيبوبروفين."
    },
    "كوفيد-19": {
        "keywords": ["كحة", "حرارة", "فقدان الشم", "فقدان التذوق", "تعب", "إرهاق", "ضيق تنفس"],
        "advice": "اعزل نفسك وراقب الأعراض. استخدم مسكنات الحرارة مثل الباراسيتامول. راجع الطبيب فوراً في حال وجود ضيق تنفس أو ألم في الصدر."
    },
    "الإنفلونزا": {
        "keywords": ["حمى", "ألم عضلات", "سعال", "تعب", "صداع", "قشعريرة"],
        "advice": "الراحة ضرورية. تناول مسكنات وخذ سوائل كثيرة. يمكن استخدام الإيبوبروفين أو الباراسيتامول."
    },
    "الربو": {
        "keywords": ["ضيق تنفس", "صفير في الصدر", "كحة ليلية", "تعب بعد المجهود"],
        "advice": "تجنب المهيجات، واستخدم بخاخ الربو الموصوف. استعمل موسعات الشعب الهوائية مثل سالبيوتامول."
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms_input = request.form.get('symptoms', '').lower()
    found_diseases = []
    for disease, info in disease_data.items():
        for keyword in info["keywords"]:
            if keyword in symptoms_input:
                found_diseases.append({
                    "disease": disease,
                    "advice": info["advice"]
                })
                break

    if not found_diseases:
        message = "لم يتم التعرف على الحالة، يرجى استشارة طبيب مختص."
        return render_template('result.html', results=None, message=message)

    return render_template('result.html', results=found_diseases, message=None)

if __name__ == '__main__':
    app.run(debug=True)
