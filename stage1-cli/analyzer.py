import sys

print("--- ЦУП: АНАЛИЗАТОР БОРТОВЫХ ЛОГОВ ЗАПУЩЕН ---")
try:
    with open("/data/raw_log.txt", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("ОШИБКА: Файл /data/raw_log.txt не найден!")
    sys.exit(1)

criticals = [line.strip() for line in lines if "[CRIT]" in line]

with open("/data/incident_report.txt", "w") as out:
    out.write("ОТЧЁТ ОБ АВАРИЯХ:\n")
    for item in criticals:
        out.write(f"- {item}\n")

print(f"Обработка завершена. Найдено аварийных записей: {len(criticals)}")
print("Файл incident_report.txt сохранён на диск хоста.")
