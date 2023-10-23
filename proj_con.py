# create a list for adjectives and verbs
adj = list()
verb = list()
noun = list()
hobby = list()
business_skill = list()

# prompt the user for adjectives, nouns,  verbs, hobby, and skills
i = 0
while i < 15:
    adj_inp = input("adjective: ")
    i += 1
    verb_inp = input("verb: ")
    i += 1
    noun_inp = input("noun: ")
    i += 1
    hobby_inp = input("hobby: ")
    i += 1
    business_skill_inp = input("business skill: ")
    i += 1
    adj.append(adj_inp)
    verb.append(verb_inp)
    noun.append(noun_inp)
    hobby.append(hobby_inp)
    business_skill.append(business_skill_inp)

print(f"I love {hobby[0]}, it makes me feel {adj[0]}. Whenever I am {hobby[1]}, it seems like the entire world before me is {adj[1]}. Have you ever met a {noun[0]}, you would need to have {business_skill[0]} just to be able to {verb[0]} out of a conversation. In one word I can describe the animal kingdom, and that word is {adj[2]}. The reason I say that is because I {hobby[2]}, so I get to {verb[1]}, I have developed my {business_skill[1]} through that, and let me just say,\" {verb[2]} \" isn't fun at all. Two things that come to mind when I hear beautiful are: {noun[1]}, and {noun[2]}. I have developed a kick for {business_skill[2]} because of that.")