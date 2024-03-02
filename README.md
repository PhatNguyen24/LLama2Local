# LLama2Local
Ask questions without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. 

Built with [LangChain](https://github.com/hwchase17/langchain), [LlamaCpp](https://github.com/ggerganov/llama.cpp)

<!-- <img width="902" alt="demo" src="https://user-images.githubusercontent.com/721666/236942256-985801c9-25b9-48ef-80be-3acbb4575164.png"> -->

# Environment Setup
In order to set your environment up to run the code here, first install all requirements:

```shell
pip install -r requirements.txt
```

Then, download the LLM model and place it in a directory of your choice:
- LLM: default to [llama-2-7b-chat.Q4_K_M.gguf](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf). 

## Ask questions, locally!
In order to ask a question, run a command like:

```shell
python run.py
```

Hit enter. You'll need to wait 2-30 seconds (depending on your machine) while the LLM model prepares the answer.

Note: you could turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

# Disclaimer
This is a pilot project to validate the feasibility of a completely private solution to question answering using LLM. It is not ready for production and should not be used in production. Model selection is not optimized for performance but for privacy; but different models and vector stores can be used to improve performance.