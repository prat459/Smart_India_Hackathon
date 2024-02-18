
from typing import List, Text, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import matplotlib.pyplot as plt
from io import BytesIO
import base64, os

class ActionSayData(Action):
    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve slot values
        bo = tracker.get_slot("bo")
        musculature = tracker.get_slot("musculature")
        st = tracker.get_slot("st")
        ht = tracker.get_slot("ht")
        wga = tracker.get_slot("wga")
        fbh = tracker.get_slot("fbh")
        m = tracker.get_slot("m")
        w = tracker.get_slot("w")
        i = tracker.get_slot("i")
        me = tracker.get_slot("me")
        c = tracker.get_slot("c")
        ins = tracker.get_slot("ins")
        mem = tracker.get_slot("mem")
        a = tracker.get_slot("a")
        d = tracker.get_slot("d")



        # Check if all required slots are set
        required_slots = ['bo', 'musculature', 'st', 'ht', 'wga', 'fbh', 'm', 'w', 'i', 'me', 'c', 'ins', 'mem', 'a', 'd']
        for slot in required_slots:
            if not locals().get(slot):
                dispatcher.utter_message(text=f"Sorry, the '{slot}' slot is not set.")
                return []

        # Dosha characteristics lists
        v = ["thin", "weakly developed", "dry", "oily", "Recalcitrant(Hard to put on weight)", "Frequent", "brisk",
             "cold intolerant", "Compromised", "reasonable", "Talkative", "responsive", "deficient retention",
             "Fast, movement, speech disorders"]

        p = ["medium", "moderate", "soft", "thick", "Fluctuating", "irregular", "Balanced", "heat intolerant",
             "Great", "Quick", "Incisive","Sharp", "Medium", "tolerable retention", "Normal", "Ulcers"]

        k = ["broad", "well-developed", "smooth and firm", "prone to breaks", "Obesity",
             "Low capacity to digest food", "Less mobile", "cold and heat intolerant", "excellent", "Poor",
             "less vocal", "Slow", "good retention", "Steady", "diabetes, atherosclerotic conditions"]

        # Initialize dosha counters
        vata = 0
        pitta = 0
        kapha = 0

        # Compare slot values to dosha characteristics
        for slot_value in [bo, musculature, st, ht, wga, fbh, m, w, i, me, c, ins, mem, a, d]:
            if slot_value in v:
                vata += 1
            elif slot_value in p:
                pitta += 1
            elif slot_value in k:
                kapha += 1

        total = vata + pitta + kapha

        vp = (vata / total) * 100
        pp = (pitta / total) * 100
        kp = (kapha / total) * 100

        if vp > pp and vp > kp:
            dispatcher.utter_message(text=f"Your dominant dosha is vata, and the percentage is {vp:.2f}%. pitta: percentage is {pp: .2f}%. kapha percentage is {kp: .2f}%")
        elif pp > vp and pp > kp:
            dispatcher.utter_message(text=f"Your dominant dosha is pitta, and the percentage is {pp:.2f}%. vata: percentage is {vp: .2f}%. kapha percentage is {kp: .2f}%")
        else:
            dispatcher.utter_message(text=f"Your dominant dosha is kapha, and the percentage is {kp:.2f}%. vata: percentage is {vp: .2f}%. pitta percentage is {pp: .2f}%")
        #
        # chart = BytesIO()
        # plt.figure(figsize=(6, 6))
        # plt.pie(dosha_percentages.values(), labels=dosha_percentages.keys(), autopct="%1.1f%%", shadow=True)
        # plt.title("Dosha Percentages")
        # plt.savefig(chart, format='png')
        # plt.close()
        #
        # # Save the chart to a publicly accessible URL (replace with your actual URL)
        # chart_url = "https://example.com/path/to/your/chart.png"
        #
        # # Provide a link to the chart in the message
        # chart_message = f"![View Pie Chart]({chart_url})"
        # dispatcher.utter_message(
        #     text=f"Your dominant dosha is {dominant_dosha}, and the percentages are as follows:\n\n{chart_message}")