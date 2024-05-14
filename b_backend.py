# 1. Connecting the BD to langchain
from langchain_community.utilities.sql_database import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///ecommerce.db")

# 2. Importing the API
import a_env_vars
import os
os.environ["OPENAI_API_KEY"] = a_env_vars.OPENAI_API_KEY

# 3. Create the LLM
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo-0125')

# 4. Create the SQLDatabaseChain
from langchain_experimental.sql import SQLDatabaseChain
cadena = SQLDatabaseChain(llm = llm, database = db, verbose=False)

# 5. Formatting the answer
formato = """
Data una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

# 6. Function to make the consult

def consulta(input_usuario):
    consulta = formato.format(question = input_usuario)
    resultado = cadena.run(consulta)
    return(resultado)
