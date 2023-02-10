import openai
import tkinter as tk

# Set the API key for OpenAI
openai.api_key = "Your apikey"

# Create the main window
root = tk.Tk()
root.title("Mini Chat GPT by Lenz Byahurwa")

# Create the input and output textboxes
input_text = tk.Text(root, height=10, width=100)
input_text.pack()

output_text = tk.Text(root, height=10, width=100)
output_text.pack()

# Create the button
def get_response():
    # Get the input from the input textbox
    user_input = input_text.get("1.0", "end-1c")

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{user_input}",
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Insert the response in the output textbox
    output_text.insert("end", response)

submit_button = tk.Button(root, text="Submit Inquiry or Question", command=get_response)
submit_button.pack()

# Start the main event loop
root.mainloop()