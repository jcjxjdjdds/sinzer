import random

# قم بتعريف مصفوفة تحتوي على الردود الممكن اختيارها
responses = [
    "أهلاً، كيف يمكنني المساعدة؟",
    "حسنًا، لدي أي سؤال آخر؟",
    "أنا هنا لمساعدتك!",
    "لا تتردد في طرح أي سؤال!",
    "أعتقد أننا يمكننا العثور على الإجابة التي تبحث عنها!"
]

# قم بتعريف دالة لاختيار وطباعة رد عشوائي
def get_random_response():
    random_index = random.randint(0, len(responses) - 1)
    print(responses[random_index])

# استدعاء الدالة للحصول على رد عشوائي
get_random_response()
