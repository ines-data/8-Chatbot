pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"say hello to (.*)|say hello (.*)",
        ["Hello %1, How are you today ?",]
    ],

    [
        r"what is your name ?",
        ["My name is Nougat and I'm a chatbot ?",]
    ],
    [
        r"sorry",
        ["Ihits alright","Its OK, never mind",]
    ],
    [
        r"hi|hey|hello|good morning",
        ["Hello", "Hey there",]
    ],
        
    [
        r"quit|Quit|Bye|bye",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

    ],
    [
        r"how are you|how are you?|how are you ?",
        ["Im good thank you ! ",]
    ],

    [
        r"thank you|thanks|good|good thanks|ok",
        ["you are welcome ! ",]
    ],

    [
        r"good|we are good",
        ["that's nice ! ",]
    ],
    
]


msg_help =  ''' ``` To help us to improve our BOT, Please proceed as below : 
!score [score] : to give your score (from 0 to 10)
!improvement [improvement_proposal] : to propose an improvement
!date now : to show the actual date&time 

Pour nous aider à améliorer notre BOT, veuillez procéder comme ci-dessous:
!score [score] : Pour donner un score (de 0 à 10)
!improvement [improvement_proposal] : Pour proposer une amélioration
!date now : Pour afficher l'heure&date actuelle 

:لمساعدتنا على تطوير هذا المنتوج، يرجى القيام بما يلي
!score [عدد] : لإعطاء تقييم
!improvement [إقتراح] : لإقتراح تطوير أو تحسين
!date now : لعرض الوقت والتاريخ الحاليين
``` 
'''