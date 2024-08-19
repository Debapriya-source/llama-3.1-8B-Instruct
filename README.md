# Llama-3.1 model test offline

## Introduction
The latest Llama🦙 (Large Language Model Meta AI) 3.1 is a powerful AI model developed by Meta AI that has gained significant attention in the natural language processing (NLP) community. It is the most capable open-source llm till date. In this blog, I will guide you through the process of cloning the Llama 3.1 model from Hugging Face🤗 and running it on your local machine using Python. After which you can integrate it in any AI project. 

---

## Prerequisites

- Python 3.8 or higher installed on your local machine
- Hugging Face Transformers library installed (`pip install transformers`)
- Git installed on your local machine
- A Hugging Face account

---


## Step 1: Get access to the model
- Click here [https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) to open the official hugging face repository of Meta's Llama-3.1-8B-Instruct (you can use other llama 3.1 models in the same way).

![Meta-llama-3.1-8b-Instruct hugging face model](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o0lpys2y71s4cte30ex7.png)

- At the beginning you should be seeing this:

![Meta-llama-3.1-8b-Instruct model](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gky1nxjvf28r46cuiwtp.png)

- Submit the form below to get access of the model

![access to meta llama 3.1 model](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/00byphoel5c8s0nfa7xw.png)

- Once you see **"You have been granted access to this model"**, you are good to go...

![gated model in hugging face](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nsttr9arstf3s7r2lp2t.png)




## Step 2: Create an ACCESS_TOKEN
- Go to **"Settings"** (Bottom right corner of the below image):

![hugging face settings](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8mfn10g0l952jn7drses.png)

- Go to **"Access Tokens"** click **"Create new token"**(upper right corner of the image):

![create hugging face token](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o43nhk25cg8e57i6u1r3.png)

- Give read and write permissions and **select the repo** as shown:

![create hugging face token](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/g15k9gxmp8vi8gdbx3cw.png)


- Copy the token and place it somewhere safe and secure as it will be needed in the future.(**note:** once you copy it you cannot copy it again, so if you anyhow forget the key, you have to create a new one to begin with :))

![huggingface token](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/175lizyojzlbkzy95pxw.png)


---


## Step 3: Clone the LLaMA 3.1 Model

Now run the following command on your favorite terminal. 
The `ACCESS_TOKEN` is the one you copied and the `<huggingface-user-name>` is the username of your hugging face account.

```Bash
git clone https://<huggingface-user-name>:<ACCESS_TOKEN>@huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct
```

This can take a lot of time depending on your internet speed.

## Step 4: Install Required Libraries

Once the cloning is done, go to the cloned folder and install all the dependencies from the `requirements.txt`. (you can create an virtual-environment using conda(**recommended**) or virtualenv)
You can find out the requirements file in my GitHub provided in the **resources** section below.

Using **conda**:
```Bash
cd Meta-Llama-3.1-8B-Instruct
conda install --yes --file requirements.txt
```
Using **pip**:
```Bash
cd Meta-Llama-3.1-8B-Instruct
pip install -r requirements.txt
```

---

## Step 5: Run the Llama 3.1 Model
Create a new Python file (e.g., test.py) and paste the location of the model repository you just cloned as the `model_id` (such as, `"D:\\Codes\\NLP\\Meta-Llama-3.1-8B-Instruct"`). Here is an example:

```Python
import transformers
import torch

## Here you paste your cloned repos location
model_id = "D:\\Codes\\NLP\\Meta-Llama-3.1-8B-Instruct" 

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "user", "content": "Who are you?"},
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])
```
You can set `device_map=cuda` if you want use the gpu also.

Step 6: Run the Python Script

```Bash
python test.py
```
### Output

![llama-3.1 output](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s2145xgibavplg0bkjvp.png)

---


## Issues you can face

- `OSError: [WinError 126] fbgemm.dll` 
   - To solve this error make sure you have **Visual Studio** installed.
     - In case you don't have it, [click here](https://visualstudio.microsoft.com/vs/community/) and install it.
     - Then restart the computer.
- If there is still any errors with pytorch versions, use [anaconda](https://www.anaconda.com/) or [miniconda](https://docs.anaconda.com/miniconda/miniconda-install/) to configure a new environment with suitable python version and dependencies.
- If you are facing any other issue or error feel free to comment below.

---

> ## Resources
> For more details on llama 3.1 check out: [https://ai.meta.com/blog/meta-llama-3-1/](https://ai.meta.com/blog/meta-llama-3-1/)

> My implementation [https://github.com/Debapriya-source/llama-3.1-8B-Instruct.git](https://github.com/Debapriya-source/llama-3.1-8B-Instruct.git) 

---

## Conclusion
In this blog, we have successfully cloned the LLaMA-3.1-8B-Instruct model from Hugging Face and run it on our local machine using Python. You can now experiment with the model by modifying the prompt, adjusting hyperparameters, or integrate with your upcoming projects. Happy coding!
