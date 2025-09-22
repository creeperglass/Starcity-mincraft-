import random

countries = {
    "ایران": {"اطلاعات": "پایتخت آن تهران است. دارای تاریخ و فرهنگ غنی است.", "قاره": "آسیا", "زبان": "فارسی", "جمعیت": "85 میلیون"},
    "فرانسه": {"اطلاعات": "پایتخت آن پاریس است. به خاطر برج ایفل و موزه لوور مشهور است.", "قاره": "اروپا", "زبان": "فرانسوی", "جمعیت": "67 میلیون"},
    "ژاپن": {"اطلاعات": "پایتخت آن توکیو است. به خاطر فناوری پیشرفته و فرهنگ سنتی معروف است.", "قاره": "آسیا", "زبان": "ژاپنی", "جمعیت": "126 میلیون"}
}

def choose_difficulty():
    print("--------------------")
    print("   ✨ تبدیل شو ✨")
    print("--------------------")
    choice = input("سطح دشواری را انتخاب کنید (آسان/متوسط/دشوار): ").strip().lower()
    if "آسان" in choice:
        return "آسان"
    elif "متوسط" in choice:
        return "متوسط"
    elif "دشوار" in choice:
        return "دشوار"
    else:
        print("انتخاب نامعتبر. سطح «متوسط» انتخاب شد.")
        return "متوسط"

def provide_hints(country, difficulty):
    if difficulty == "آسان":
        print(f"قاره: {country['قاره']}")
        print(f"زبان رسمی: {country['زبان']}")
        print(f"جمعیت: {country['جمعیت']}")
    elif difficulty == "متوسط":
        print(f"قاره: {country['قاره']}")
        print(f"زبان رسمی: {country['زبان']}")
    # دشوار: بدون راهنمایی اضافی

def print_creeper():
    creeper = [
        "🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩⬛⬛🟩🟩⬛⬛🟩",
        "🟩⬛⬛🟩🟩⬛⬛🟩",
        "🟩🟩🟩🟩🟩🟩🟩🟩",
        "🟩🟩🟩⬛⬛🟩🟩🟩",
        "🟩🟩⬛⬛⬛⬛🟩🟩",
        "🟩🟩⬛🟩🟩⬛🟩🟩"
    ]
    for line in creeper:
        print(line)

def clean_text(text):
    replacements = ["من می‌خواهم به ", "تبدیل شوم", "به ", "اها ", " هست"]
    for word in replacements:
        text = text.replace(word, "")
    return text.strip().lower()

def play_game():
    print("--------------------")
    print("   ✨ تبدیل شو ✨")
    print("--------------------")
    difficulty = choose_difficulty()
    country_name, country_info = random.choice(list(countries.items()))
    print(country_info["اطلاعات"])
    provide_hints(country_info, difficulty)

    guess = clean_text(input("نام کشور را حدس بزنید: "))
    correct_answer = country_name.strip().lower()

    if guess == correct_answer:
        transformation = clean_text(input("درست حدس زدید! شما برنده شدید. می‌خواهید به چه چیزی تبدیل شوید؟ "))
        print(f"شما به {transformation} تبدیل شدید!")
        if transformation in ["کریپر", "کربپر"]:
            print_creeper()
    else:
        print(f"اشتباه حدس زدید! پاسخ درست: {country_name} بود. شما به باد تبدیل شدید.")

# اجرای بازی
play_game()
