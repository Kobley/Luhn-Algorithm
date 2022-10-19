class LuhnUtil:
    def __init__(self, toCheck: str, card: bool):

        # Validate Number
        if not isinstance(toCheck, str):
            raise TypeError("Input Number Must Be A String.")

        self.toCheck = toCheck

        # Validate Card Check
        if not isinstance(card, bool):
            raise TypeError("Card Must Be A Boolean.")

        self.card = card

    def validate(self, toCheck: str, card: bool):
        self.__init__(toCheck, card)

    def runAlgorithm(self):
        self.validate(self.toCheck, self.card)
        reversed_numbers = [int(x) for x in self.toCheck[::-1]]
        end_digits = list()
        digits = list(enumerate(reversed_numbers, start=1))

        for index, digit in digits:
            if index % 2 == 0:
                indexed = digit * 2
                end_digits.append(indexed - 9) if indexed > 9 else end_digits.append(indexed)
            else:
                end_digits.append(digit)
        if not self.card:
            return sum(end_digits) % 10 == 0
        else:
            passes = sum(end_digits) % 10 == 0
            card_types = {
                ("34","37"):"American Express",
                ("51","52","53","54","55"):"MasterCard",
                ("4"):"Visa",
                ("36","38","300","301","302","303","304","305"):"Diners Club and Carte Blanche",
                ("6011"):"Discover",
                ("2123","1800"):"JCB"
            }
            cardInfo = {}
            if(passes):
                prefixOfNumber = self.toCheck[0:2]
                cardInfo["card_number"] = self.toCheck
                for prefixes, bank in card_types.items():
                    for prefix in prefixes:
                        if prefixOfNumber.startswith("4"):
                            cardInfo["possible_banks"] = card_types["4"]
                        elif prefixOfNumber.startswith("5"):
                            cardInfo["possible_banks"] = card_types[("51","52","53","54","55")]
                        # Should allow mastercard, AME, etc to be found but still doesnt work... Fix Soon? Manual sucks
                        elif prefixOfNumber.find(prefix):
                            cardInfo["possible_banks"] = card_types.get(prefix)
                        else:
                            cardInfo["possible_banks"] = "Unknown"
            else:
                cardInfo["card_number"] = self.toCheck
                cardInfo["possible_banks"] = "Did not pass Luhn Test"
            return cardInfo