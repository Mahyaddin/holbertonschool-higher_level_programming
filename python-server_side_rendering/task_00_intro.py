import os

def generate_invitations(template, attendees):
    # Tipləri yoxla
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    # Boş olub-olmamasını yoxla
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Emal və Fayl yaratma
    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            val = attendee.get(key)
            content = content.replace(f"{{{key}}}", str(val) if val is not None else "N/A")
        
        with open(f"output_{i}.txt", "w", encoding="utf-8") as f:
            f.write(content)