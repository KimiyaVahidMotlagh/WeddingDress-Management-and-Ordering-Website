# recommendation/attribute_recommender.py
class AttributeRecommender:
    """Base strategy class for recommending dress attributes."""

    def recommend(self, body_type: str) -> dict:
        raise NotImplementedError("Subclasses must implement recommend()")


class RuleBasedRecommender(AttributeRecommender):
    """Rule-based recommender using fashion heuristics."""

    def __init__(self):
        # Simple rules, can be expanded or replaced with ML models
        self.rules = {
            "hourglass": {
                "sleeve": "cap sleeve or sleeveless",
                "neckline": "sweetheart or V-neck",
                "bodice": "fitted corset",
                "skirt": "mermaid or trumpet",
                "train": "chapel length",
                "structure": "structured waistline"
            },
            "pear": {
                "sleeve": "off-shoulder or strapless",
                "neckline": "boat or scoop",
                "bodice": "fitted top, embellished bodice",
                "skirt": "A-line or ball gown",
                "train": "cathedral",
                "structure": "flared skirt balance"
            },
            "apple": {
                "sleeve": "3/4 sleeve",
                "neckline": "deep V-neck",
                "bodice": "empire waist",
                "skirt": "A-line flowy",
                "train": "sweep train",
                "structure": "draped fabrics"
            },
            "rectangle": {
                "sleeve": "spaghetti strap",
                "neckline": "halter or sweetheart",
                "bodice": "ruched corset",
                "skirt": "ball gown or layered tulle",
                "train": "chapel train",
                "structure": "accentuated waist"
            },
            "petite": {
                "sleeve": "strapless",
                "neckline": "V-neck",
                "bodice": "simple fitted bodice",
                "skirt": "sheath or empire",
                "train": "no train or sweep train",
                "structure": "elongated silhouette"
            }
        }

    def recommend(self, body_type: str) -> dict:
        return self.rules.get(body_type.lower(), {
            "sleeve": "custom",
            "neckline": "custom",
            "bodice": "custom",
            "skirt": "custom",
            "train": "custom",
            "structure": "custom"
        })


# برای تست
if __name__ == "__main__":
    recommender = RuleBasedRecommender()
    print("Hourglass body type recommendation:")
    print(recommender.recommend("hourglass"))