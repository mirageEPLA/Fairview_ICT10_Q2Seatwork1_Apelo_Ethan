from pyscript import Element

# Club members list
members = ["Ethan", "Juan Gomez", "John Cruz", "Victor Gonzales"]

def check_member(event=None):
    fname = document.getElementById("fname").value.strip()
    lname = document.getElementById("lname").value.strip()
    full_name = f"{fname} {lname}"

    # Dictionary mapping names to messages (no conditionals/loops)
    messages = {
        **{name: f"Congratulations {name}! You are now part of the ICT club." for name in members},
        **{full_name: f"Sorry {full_name}, your name is not on the list."}
    }

    Element("result").write(messages[full_name])
