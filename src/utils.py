import base64

def classify_name(name):
    classes = {  
        "stores" : [
            "Walmart",
            "Target",
            "Costco",
            "Best Buy",
            "Home Depot",
            "Lowe's",
            "Kroger",
            "Safeway",
            "Trader Joe's",
            "Whole Foods Market",
            "Walgreens",
            "CVS",
            "7-Eleven",
            "Macy's",
            "Nordstrom",
            "Bloomingdale's",
            "JCPenney",
            "Saks Fifth Avenue",
            "Neiman Marcus",
            "Barneys New York",
            "Gap",
            "Old Navy",
            "H&M",
            "Zara",
            "Uniqlo",
            "Levi's",
            "Nike",
            "Adidas",
            "Puma",
            "Reebok",
            "bazar",
            "traders",
            "Barnes & Noble",
            "Books-A-Million",
            "Office Depot",
            "Staples",
            "Bed Bath & Beyond",
            "Pottery Barn",
            "Crate & Barrel",
            "IKEA",
            "Pier 1 Imports",
            "World Market",
            "Michaels",
            "Joann Fabrics",
            "Hobby Lobby",
            "CVS Pharmacy",
            "Rite Aid",
            "Local Grocer",
            "Market",
            "Boutique",
            "Shop",
            "store",
            "center",
            "electrical",
            "medical",
            "salon",
            "motor",
            "motors",
            "agency",
            "foot"
            
        ],
        "family" : [
            "Mother", "Mom", "Mummy", "maa","ghar",
            "Father", "Dad", "Papa",
            "Brother", "Bhai", "bro",
            "Sister", "Bahan", "Bhn",
            "Grandmother", "Grandma", "Granny", "Nana", "Nani", "Dadi",
            "Grandfather", "Grandpa", "Granddad", "Nana", "Nanu", "Dadu",
            "Aunt", "Chachi", "Mami", "Mausi", "Fua",
            "Uncle", "Chacha", "Mama", "Maasa", "Fufaji",
            "Cousin", "Cousin Brother", "Cousin Sister",
            "Son", "Beta",
            "Daughter", "Beti",
            "Nephew", "Bhatija", "Bhanja",
            "Niece", "Bhatiji", "Bhanji",
            "Husband", "Patidev",
            "Wife", "Patni",
            "Mother-in-law", "Saas",
            "Father-in-law", "Sasur",
            "Brother-in-law", "Jeeja", "Devar", "Nandoi",
            "Sister-in-law", "Bhabhi", "Nanad",
        ],
        "fuel" : [
            "fuel fump",
            "fuel",
            "pump",
            "petrol",
            "diesel",
            "oil"
        ],
        "ecommerce" : [
            "Amazon",
            "Flipkart",
            "Meesho",
            "blinkit",
            "Snapdeal",
            "Myntra",
            "Jabong",
            "ShopClues",
            "BigBasket",
            "Nykaa",
            "Paytm Mall",
            "Flipkart Wholesale",
            "AJIO",
            "Pepperfry",
            "Urban Ladder",
            "Lenskart",
            "Fynd",
            "Tatacliq",
            "Reliance Digital",
            "Croma",
            "Zivame",
            "H&M",
            "Sephora",
            "Smytten",
            "BookMyShow",
            "Grofers",
            "Shoppers Stop",
            "Vijay Sales",
            "Kalki Fashion",
            "Saree.com",
            "Rite Aid",
            "Walgreens",
            "CVS",
            "Best Buy",
            "Newegg",
            "Overstock",
            "Wayfair",
            "Etsy",
            "AliExpress",
            "JD.com",
            "Rakuten",
            "ASOS",
            "Boohoo",
            "Zalando",
            "The Hut",
            "Argos",
            "Marks & Spencer",
            "John Lewis",
            "Boots"
        ],
        "food" : [
            "chat",
            "food",
            "Swiggy",
            "restaurant"
            "Zomato",
            "Pizza Hut",
            "Domino's Pizza",
            "Burger King",
            "McDonald's",
            "KFC",
            "Subway",
            "bar",
            "milk",
            "dairy",
            "sweets",
            "Starbucks",
            "Cafe","Coffee",
            "Dunkin' Donuts",
            "Taco Bell",
            "Pani Puri",
            "Chaat",
            "Idli Center",
            "Chinese",
            "Samosa",
            "curry",
            "Biryani",
            "Momo",
            "Pasta",
            "BBQ Nation",
            "Buffet",
            "Dosa",
            "Falafel Stand",
            "Tandoori Junction",
            "Noodles House",
            "Gourmet Grill",
            "Sweet Tooth Bakery",
            "Ice Cream Parlor",
            "Doner Kebab",
            "Waffle House",
            "Crepe Cafe",
            "Smoothie Stop",
            "Vegan Cafe",
            "Health Food Corner",
            "Food Truck Fiesta",
            "Caterer Express",
            "Local Diner",
            "Gourmet Bistro",
            "Lunchbox Delivery",
            "Sushi Express",
            "Bagel Bakery",
            "Tea",
            "Popcorn Palace"
        ],
        "recharges_and_bills" : [
            "Recharge",
            "Bill",
            "Payment",
            "Top-up",
            "Subscription",
            "Prepaid",
            "Postpaid",
            "Account",
            "Service",
            "Balance",
            "Invoice",
            "Charge",
            "Fee",
            "Credit",
            "Debit",
            "Monthly",
            "Annual",
            "Utility",
            "Deposit",
            "Transaction",
            "Electronic",
            "Automated",
            "Online",
            "Mobile",
            "Prepay",
            "Renewal",
            "Settlement",
            "Adjustment",
            "Confirmation",
            "Update",
            "Processing",
            "Processing Fee",
            "Confirmation Fee",
            "Service Fee",
            "Usage",
            "Amount",
            "Due",
            "Outstanding",
            "Statement",
            "Settlement",
            "Transaction ID",
            "Reference",
            "Billing Cycle",
            "Service",
            "Discount",
            "Penalty",
            "Fine",
            "Credit Balance",
            "Debit Balance",
            "Account Balance",
            "Payment Gateway",
            "Billing Platform",
            "Digital Payment",
            "Recurring",
            "One-time",
            "Invoice Number",
            "Payment Method"
        ],
        "donation" : [
            "Foundation",
            "Charity",
            "Fund",
            "Trust",
            "Relief",
            "Association",
            "Aid",
            "Help",
            "Support",
            "Mission",
            "Project",
            "Campaign",
            "Alliance",
            "Network",
            "Initiative",
            "Action",
            "Group",
            "Organization",
            "Society",
            "Committee",
            "Institute",
            "Agency",
            "Relief Fund",
            "Giving",
            "Philanthropy",
            "Welfare",
            "Endowment",
            "Appeal",
            "Wellbeing",
            "Compassion",
            "Rescue",
            "Empowerment",
            "Volunteers",
            "Partnership",
            "Benefactors",
            "Advocacy",
            "Outreach",
            "Missionaries",
            "Goodwill",
            "Hope",
            "Care",
            "Healing",
            "Development",
            "Sustainability",
            "Generosity",
            "Charitable Trust",
            "Donor Network",
            "Grants",
            "Endowment Fund",
            "Philanthropic Foundation"
        ]
    }

    for keys in classes.keys():
        for keyword in classes[keys]:
            if keyword.lower() in name.lower():
                return keys
    return "Individual"



def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None

