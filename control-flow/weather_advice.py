current_whether=input("What's the weather like today? (sunny/rainy/cold):")
if current_whether.lower()=="sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_whether.lower()=="rainy":
    print("Don't forget your umbrella and a raincoat.")

elif current_whether.lower()=="cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")