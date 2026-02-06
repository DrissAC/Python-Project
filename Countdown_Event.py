from datetime import datetime, timedelta
import time

def get_event_datetime():
    try:
        date_input = input("Entrez la date de l'evenement (JJ/MM/AAAA HH:MM:SS): ")
        return datetime.strptime(date_input, "%d/%m/%Y %H:%M:%S")
    except ValueError:
        print("Format de date incorrect. Veuillez utiliser le format JJ/MM/AAAA HH:MM:SS.")
        return None
    
def calculate_time_remaining(event_date):
    current_date = datetime.now()
    time_difference = event_date - current_date
    return time_difference

def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\nTemps restant: {days} jours, {hours} heures, {minutes} minutes, {seconds} secondes.", end="")

def start_countdown(event_date):
    while True:
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
            print("\nL'evenement est arrivé !")
            break
        display_countdown(time_left)
        time.sleep(1)

event_datetime = get_event_datetime()
if event_datetime:
    print(f"Evenement prévu pour le {event_datetime.strftime('%d/%m/%Y %H:%M')}")
    start_countdown(event_datetime)