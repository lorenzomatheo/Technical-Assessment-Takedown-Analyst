import boto3
import json

prompt_template = """
Você é um analista de cibersegurança que responde somente na língua português brasileiro. Para o link abaixo, forneça:

1. Identificação: O link é suspeito? Por quê?
2. Notificação: Quem deve ser notificado?
3. Mensagem: Gere um e-mail formal sobre a ameaça.

Link: {url}
"""

bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

urls = [
    "https://recthall[.]com/access/",
    "https://feiraodeoferta[.]com[.]br/acordo",
    "https://sicredi.meuacesso[.]org[.]uk/index.php?acesso=189.6.247.160&localizacao=Brazil",
    "http://piqmi[.]top/atawKCbb/02828560951690613024ac1689"
]

for url in urls:
    prompt = prompt_template.format(url=url)
    response = bedrock.invoke_model(
        modelId="mistral.mistral-7b-instruct-v0:2",
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "prompt": prompt,
            "max_tokens": 512,
            "temperature": 0.2,
            "top_p": 0.9
        })
    )
    result = json.loads(response['body'].read())
    print(f"\n🔍 Analisando: {url}")
    generated_text = result["outputs"][0]["text"]
    print(generated_text)
