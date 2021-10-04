# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.events import FollowupAction
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
from rasa_sdk.events import Restarted
from weather import Weather
import yaml
import random



class UserForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "age"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 age=tracker.get_slot("age"))

        return[]


class ActionlinkStudy(Action):

    def name(self) -> Text:
        return "action_study"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


       
        dispatcher.utter_message(text='[Some useful carrer paths](https://www2.deloitte.com/us/en/insights/deloitte-review/issue-21/changing-nature-of-careers-in-21st-century.html)')

        return []


class ActionlinkMovie(Action):

    def name(self) -> Text:
        return "action_movie"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


       
        dispatcher.utter_message(text='[Best Movies of all time](https://www.imdb.com/chart/top/)')

        return []



class ActionYoutubeVideos(Action):

    def name(self) -> Text:
        return "action_play_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Hello World!")
        dispatcher.utter_message(attachment={
            "type": "video",
            "payload": {
                "title": "This video will help you to relax, just close your eyes and put on your headphones :) ",
                "src": "https://www.youtube.com/embed/9BD1y0TOk3o"
            }
        })

        return []
        

class Actionexercise(Action):
     
    def name(self) -> Text:
        return "action_exercise"

    def run(self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message(attachment={
            "type": "video",
            "payload": {
                "title": "let's try some yoga :) ",
                "src": "https://www.youtube.com/embed/EwQkfoKxRvo"
            }
        })
   
        dispatcher.utter_message(attachment={
            "type": "video",
            "payload": {
                "title": "let's try some workout :) ",
                "src": "https://www.youtube.com/embed/24fdcMw0Bj0"
      
             }
        })
       

        return []

class Actionweather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city=tracker.latest_message['text']
        temp=int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp",tracker,temp=temp)

        return []

def que():  

    with open(r'C:\Users\Home\Desktop\cori2_up1\data\phq9.yml') as f:  
        quest = yaml.safe_load(f)
        question = quest['questions']   
        
    return question  

v = []    
c = 0
i = 0
p = []
total = 0
b = None
check = False

class ActionQuestion(Action):

    def name(self):

        return "action_question"

    def run(
        self, dispatcher, tracker: Tracker,
        domain: Dict[Text, Any]) -> List[EventType]:
        
    
        q_id = tracker.get_slot('q_id')
   
        global c
        global v
        global i
        global p
        global total
        global b
        global check 
  

     
       
        if c <=2 and ( b == 0 or b== 1) and check == False:
            if c <=2:

                per = int(tracker.get_slot('score_value'))  
                p.append(per)
              
                print('ra')
                print(p)
                if c == 2:
                    dispatcher.utter_message(text = "that's a lot for today, will ask more question later !")
                    for  x in range(0,len(p)):
                        total = total + p[x]
                    if total == 0:
                        dispatcher.utter_message(text = "I have calculated values provided by you for the questions asked:")
                        dispatcher.utter_message(text = "It seems you are doing perfectly fine, there is nothing to worry. Keep up the good work!")
                
                
        if c < 2:
            a = que() 
            # b = a.index(a[i]) 
            b = random.randrange(len(a))
            print(b)
            print(a[b]) 
          
         
            if b not in v:            
              
                   
                if b == 0:
                    dispatcher.utter_message(text=a[b])
                    dispatcher.utter_message(template= 'utter_question1')
                    # dispatcher.utter_message(template = 'utter_question_1')
                    check = False
                    
                   
                 
                    
                       
                 
                elif b == 1 :
                    dispatcher.utter_message(text = a[b])
                    dispatcher.utter_message(template= 'utter_question1')
                    # dispatcher.utter_message(template = 'utter_question_2')
                    check = False
                  
       
                # # elif i == 2 and qnu == 2:
                    # # dispatcher.utter_message(template = "utter_3")
                

           
                
                v.append(b)   
                print(v) 
               
                                    
                i+=1
                c+=1       
                print(c)
                print(i)
                return[SlotSet('q_id',b)]
                
 
              
                

        
        
        # if c == 2:
            # dispatcher.utter_message(text = 'thats for now')
        
            elif b in v and c < 2: 
                check = True
                return [FollowupAction("action_question")]  
                
               
        return []     
            

# class Actionnextquestion(Action):
    # def name(self) -> Text:
        # return "action_next_question"

    # def run(
        # self,
        # dispatcher: CollectingDispatcher,
        # tracker: Tracker,
        # domain: Dict[Text, Any],
    # ) -> List[EventType]:
        # next = tracker.get_slot("next_question")
        
        # if next == 'no please':
            # dispatcher.utter_message(template = 'utter_bye')

        # else:
            # return [FollowupAction("action_question")]

counter = 0
class Actionnextquestion(Action):
    def name(self) -> Text:
        return "action_next_question"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        global counter 
        counter+=1
        
        if counter <= 2:
            return [FollowupAction("action_question")]
        # else:
            # dispather.utter_message(text= '')

# class Actionfeedback(Action):
    # def name(self) -> Text:
        # return "action_feedback"

    # def run(
        # self,
        # dispatcher: CollectingDispatcher,
        # tracker: Tracker,
        # domain: Dict[Text, Any],
    # ) -> List[EventType]:
        # dispatcher.utter_message(template="utter_thanks_suggestion")
        # return []


class Actionarticle(Action):

    def name(self) -> Text:
        return "action_article"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


       
        dispatcher.utter_message(text='[Best article: 1](https://patient.info/news-and-features/how-to-boost-self-esteem)')
        dispatcher.utter_message(text='[Best article: 2](https://www.helpguide.org/articles/depression/depression-treatment.htm)')
        
        dispatcher.utter_message(attachment={
            "type": "video",
            "payload": {
                "title": "This video will sure boost your confidence and help you come out of your depression :) ",
                "src": "https://www.youtube.com/embed/oHi4fCuB4u0",
                "src": "https://www.youtube.com/embed/cWBYTAqKeHw"
            }
        })
        

        return []

class ActionSubmitSuggestionForm(Action):
    def name(self) -> Text:
        return "action_submit_suggestion_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message(template="utter_thanks_suggestion")
        return []


# class ActionStoreBotLanguage(Action):
    # """Takes the bot language and checks what pipelines can be used"""

    # def name(self) -> Text:
        # return "action_store_bot_language"

    # def run(
        # self,
        # dispatcher: CollectingDispatcher,
        # tracker: Tracker,
        # domain: Dict[Text, Any],
    # ) -> List[EventType]:
        # spacy_languages = [
            # "english",
            # "french",
            # "german",
            # "spanish",
            # "portuguese",
            # "french",
            # "italian",
            # "dutch",
        # ]
        # language = tracker.get_slot("language")
        # if not language:
            # return [
                # SlotSet("language", "that language"),
                # SlotSet("can_use_spacy", False),
            # ]

        # if language.lower() in spacy_languages:
            # return [SlotSet("can_use_spacy", True)]
        # else:
            # return [SlotSet("can_use_spacy", False)]
            
# def tag_convo(tracker: Tracker, label: Text) -> None:
    # """Tag a conversation in Rasa X with a given label"""
    # endpoint = f"http://{config.rasa_x_host}/api/conversations/{tracker.sender_id}/tags"
    # requests.post(url=endpoint, data=label)
    # return


# class ActionTagFeedback(Action):
    # """Tag a conversation in Rasa X as positive or negative feedback """

    # def name(self):
        # return "action_tag_feedback"

    # def run(
        # self,
        # dispatcher: CollectingDispatcher,
        # tracker: Tracker,
        # domain: Dict[Text, Any],
    # ) -> List[EventType]:

        # feedback = tracker.get_slot("feedback_value")

        # if feedback == "positive":
            # label = '[{"value":"postive feedback","color":"76af3d"}]'
        # elif feedback == "negative":
            # label = '[{"value":"negative feedback","color":"ff0000"}]'
        # else:
            # return []

        # tag_convo(tracker, label)

        # return []



