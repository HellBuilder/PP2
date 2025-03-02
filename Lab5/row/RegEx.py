import re

file_path = r"C:\Users\Admin\Desktop\PP2-Repos\PP2\TSIS5_LAB5\row\row.txt"
with open(file_path, "r", encoding="utf-8") as file:
    receipt_text = file.read()

header_pattern = re.search(
    r"(ДУБЛИКАТ.*?)\nКассир\s+([\w\s-]+)", receipt_text, re.DOTALL
)
header_info = header_pattern.group(1) if header_pattern else "Не найдено"
cashier_name = header_pattern.group(2) if header_pattern else "Не найдено"

items_pattern = re.findall(
    r"(\d+)\.\n(.*?)\n(\d+,\d{3}) x ([\d\s]+,\d{2})\n([\d\s]+,\d{2})",
    receipt_text,
    re.DOTALL
)

total_pattern = re.search(r"ИТОГО:\s+([\d\s]+,\d{2})", receipt_text)
total_amount = total_pattern.group(1) if total_pattern else "Не найдено"

payment_pattern = re.search(r"Банковская карта:\s+([\d\s]+,\d{2})", receipt_text)
payment_amount = payment_pattern.group(1) if payment_pattern else "Не найдено"

datetime_pattern = re.search(r"Время:\s+(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})", receipt_text)
transaction_time = datetime_pattern.group(1) if datetime_pattern else "Не найдено"

fiscal_pattern = re.search(r"Фискальный признак:\s+(\d+)", receipt_text)
fiscal_number = fiscal_pattern.group(1) if fiscal_pattern else "Не найдено"

address_pattern = re.search(r"г\.\s*Нур-султан.*", receipt_text)
store_address = address_pattern.group(0) if address_pattern else "Не найдено"

operator_pattern = re.search(r"Оператор фискальных данных:\s+(.+)", receipt_text)
operator_info = operator_pattern.group(1) if operator_pattern else "Не найдено"

ink_ofd_pattern = re.search(r"ИНК ОФД:\s+(\d+)", receipt_text)
ink_ofd = ink_ofd_pattern.group(1) if ink_ofd_pattern else "Не найдено"

kkm_rnm_pattern = re.search(r"Код ККМ КГД \(РНМ\):\s+(\d+)", receipt_text)
kkm_rnm = kkm_rnm_pattern.group(1) if kkm_rnm_pattern else "Не найдено"

znm_pattern = re.search(r"ЗНМ:\s+([\w\d]+)", receipt_text)
znm = znm_pattern.group(1) if znm_pattern else "Не найдено"

print("===== ФИСКАЛЬНЫЙ ЧЕК =====")
print(header_info)
print(f"\nКассир: {cashier_name}")
print(f"Время: {transaction_time}")
print(f"Фискальный признак: {fiscal_number}")
print(f"Адрес: {store_address}")
print("\nКупленные товары:")
print("=" * 120)
print(f"{'№':<5} {'Товар':<40} {'Кол-во':<10} {'Цена':<10} {'Всего'}")
print("=" * 120)

if items_pattern:
    for item in items_pattern:
        num = item[0]
        item_name = item[1].strip()
        qty = item[2].strip()
        price = item[3].replace(" ", "").strip()
        total = item[4].replace(" ", "").strip()
        print(f"{num:<5} {item_name:<40} {qty:<10} {price:<10} {total}")
else:
    print("Ошибка: Товары не найдены. Проверьте формат чека.")

print("\n" + "=" * 120)
print(f"Способ оплаты: Банковская карта - {payment_amount}")
print(f"Всего: {total_amount}")
print("=" * 120)

print(f"\nОператор фискальных данных: {operator_info}")
print("Для проверки чека зайдите на сайт: consumer.oofd.kz")
print(f"\nИНК ОФД: {ink_ofd}")
print(f"Код ККМ КГД (РНМ): {kkm_rnm}")
print(f"ЗНМ: {znm}")
print("\nWEBKASSA.KZ")
print("=" * 120)
