print("\U0001f600")
import emoji
print(emoji.emojize(":grinning_face_with_big_eyes:"))
#print(emoji.EMOJI_ALIAS_UNICODE_ENGLISH)
word_to_emoji = {
    "happy" : emoji.emojize(":grinning_face_with_big_eyes:"),
    "great" : emoji.emojize(":thumbs_up:")
}
print(word_to_emoji["great"])
sentance = input("Enter a sentance: ")
sentance = sentance.split(" ")
for word in range(len(sentance)):
    if sentance[word] in word_to_emoji:
        sentance[word] = word_to_emoji[sentance[word]]
sentance = " ".join(sentance)
print(sentance)