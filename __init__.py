# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill
from mycroft.skills.core import MycroftSkill, intent_handler

# Creating HelloWorldSKill extending MycroftSkill
class DogWalkingSkill(MycroftSkill):
    
    def __init__(self):
        super(DogWalkingSkill, self).__init__("DogWalkingSkill")

    # def initialize(self):
    #     # Creating GreetingsIntent requiring Greetings vocab
    #     wweather = IntentBuilder("WWeatherIntent").require("query").require("WWeather").build()
    #     # Associating a callback with the Intent
    #     self.register_intent(wweather, self.handle_wweather)
    #     walk = IntentBuilder("WalkIntent").require("query").require("Walk1").build()
    #     self.register_intent(walk, self.handle_walk)

    @intent_handler(IntentBuilder("WWeatherIntent").require("query").require("WWeather").build())
        
    def handle_wweather(self):
        self.speak_dialog("WWeather")

    
    @intent_handler(IntentBuilder("WhenWalkIntent").require("firstq").require("whenwalk").build())

    def handle_whenwalk(self):
        self.speak_dialog("When")
   
    def stop(self):
        pass


def create_skill():
    return DogWalkingSkill()