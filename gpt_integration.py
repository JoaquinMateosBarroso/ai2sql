import openai

def setupfor_sql():
    openai.api_key = "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"
    prompt = "Tengo una base de datos SQL en la que hay una tabla \"usuarios\" con los atributos \"nombre\" y \"dni\", y hay una tabla \"datos\" con los atributos \"dni\"(clave foránea de usuarios) y \"direccion\". De ahora en adelante respóndeme únicamente con las sentencias que resuelven las consultas que te voy a pedir."
    completion = openai.Completion.create(engine="text-davinci-002",
                                          prompt=prompt,
                                          max_tokens=100)
    return completion

def pediryresponder_sql():
    prompt = input("¿Qué consulta quieres hacer? \n(Escribe 'salir' para terminar el programa) \n")
    completion = openai.Completion.create(engine="text-davinci-002",
                                          prompt=prompt,
                                          max_tokens=100)
    return completion
    
print(setupfor_sql().choices[0].text)
print(pediryresponder_sql().choices[0].text)

