from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import LlamaCpp

#prompt
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

DEFAULT_SYSTEM_PROMPT="""\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

instruction = "Convert the following text from English to French: \n\n {text}"

SYSTEM_PROMPT = B_SYS + DEFAULT_SYSTEM_PROMPT + E_SYS

template = B_INST + SYSTEM_PROMPT + instruction + E_INST
prompt = PromptTemplate(template=template, input_variables=["text"])
#
# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Make sure the model path is correct for your system!
n_gpu_layers = -1  # The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
n_batch = 1024  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
llm = LlamaCpp(
            model_path="./models/llama-2-7b-chat.Q4_K_M.gguf",
            n_gpu_layers=n_gpu_layers,
            n_batch=n_batch,
            callback_manager=callback_manager,
            verbose=True,  # Verbose is required to pass to the callback manager
            n_ctx=2048
)

llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "how are you"
llm_chain.run(question)
