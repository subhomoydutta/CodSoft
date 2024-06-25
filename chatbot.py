data={
    "hi":"Hi there! I am a chatbot.i here to assist you.presently i can help you in few topics.like,ISRO,NASA and ESA.",
    "good morning":"good morning.",
    "good afternoon":"good afternoon.",
    "good evening":"good evening",
    "good night":"good night, have a nice sleep.",
    "hello":"Hello! How can I help you today? presently i can help you in few topics.like,ISRO,NASA and ESA.",
    "what is your name":"I'm a chatbot,and my name is RONI,you can also call me ChatBot.what is your name?",
    "subhomoy":"oo...nice to meet you.",
    "CodSoft":"it is my please to meet you people from Codsoft.",
    "what is ISRO":"ISRO is the national space agency of INDIA.established in the year 15th august 1969.",
    "more on ISRO":"i am sorry for the inconvinience caused.for further information please visit the link https://www.isro.gov.in .please do ask me if you want to know about something else.",
    "more about ISRO":"i am sorry for the inconvinience caused.for further information please visit the link https://www.isro.gov.in .please do ask me if you want to know about something else.",
    "thank you":"you are most welcome:)",
    "what is NASA":"it stands for National Areonautics and Space Administration.it is the government space agency of United States responsible for space technology, earth and space scienceand aeronautics research",
    "more on NASA":"for more information please visit https://wwww.nasa.gov .if you have any more queries,you can ask me.",
    "more about NASA":"for more information please visit https://wwww.nasa.gov .if you have any more queries,you can ask me.",
    "what is ESA":"ESA stands for European Space Agency,which was established in the year 30th may,1975, Europe.",
    "more on ESA":"please follow the given link https://www.esa.int .fell free to ask if you have any more query.",
    "more about ESA":"follow the given link https://www.esa.int .fell free to ask if you have any more query.",
    "where are you from":"I'm from the digital world, SUBHOMOY DUTTA from INDIA made me for his internship project at CodSoft.",
    "when were you created":"i was created by SUBHOMOY DUTTA as an internship project from codsoft,on 26/06/2024.",
    "how are you":"I'm a chatbot and hence have no life.",
    "bye":"Bye! Take care and have a great day!",
}
def get_response(user_input):
    for pattern,response in data.items ():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't get you.Can you please rephrase your sentence or ask me something else?"
print("Chatbot: Hi! I'm a chatbot,I'm here to assist you! please do start the conversation with 'hi' or 'hello'.")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Chatbot: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Chatbot:",response)