import module as md

def handle_response(message):
    message.strip()
    message1 = message.split(' ')
    if message1[0] == '!help':
        return 'Im here to help you choose your most suitable career! just write !start and we will begin!'+'\n'+'Please, when you !start write the list of grades (1-100) and preferences (1-10) in the following order and format: math, Written Expression, Natural Sciences, Foreign Language, Social Sciences, Humanities preference, Engineering preference, Science preference, Health preference'
    elif message1[0] == '!about':
        return 'My name is Jaime and this is my guide bot for students! I will use your grades and personal preferences to set you up with your dream career'
    elif message1[0] == '!start':
        e = []
        for gr in message1[1].split(','):
            e.append(int(gr))

        suitableCareer = md.ruleBasedAnswer(e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8])
        
        return suitableCareer

        

    
