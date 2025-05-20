# Analisador de Links Suspeitos com AWS Bedrock

## Descrição

Este projeto é uma demonstração técnica para um Technical Assessment que utiliza o Amazon Bedrock para analisar URLs potencialmente maliciosas. O sistema emprega o modelo Mistral-7B para avaliar links suspeitos, gerando análises detalhadas de cibersegurança que incluem identificação de ameaças, recomendações de notificação e modelos de e-mail para comunicação formal sobre incidentes.

## Objetivo

O objetivo principal deste projeto é demonstrar a integração entre serviços de IA generativa (AWS Bedrock) e análise de cibersegurança, fornecendo uma ferramenta automatizada para avaliação preliminar de links suspeitos. Esta solução pode ser utilizada como primeiro passo em um processo de triagem de ameaças cibernéticas, auxiliando analistas de segurança na identificação rápida de potenciais riscos.

## Público-alvo

Este projeto é destinado a:
- Desenvolvedores interessados em integração com modelos de linguagem de grande escala (LLMs)
- Analistas de segurança que buscam automatizar processos de triagem de ameaças
- Profissionais de TI que desejam explorar casos de uso de IA generativa em cibersegurança

## Arquitetura da Solução

O sistema funciona através dos seguintes componentes:
1. **Cliente AWS Bedrock**: Interface para comunicação com os modelos de IA da AWS
2. **Modelo Mistral-7B**: LLM responsável pela análise contextual dos URLs
3. **Template de Prompt**: Estrutura que orienta o modelo a gerar análises padronizadas
4. **Processador de URLs**: Componente que itera sobre uma lista de links suspeitos

## Pré-requisitos

Para executar este projeto, você precisará de:

- Python 3.8 ou superior
- Conta AWS com acesso ao serviço Amazon Bedrock
- Permissões IAM configuradas para acessar o Bedrock
- Pacote boto3 instalado
- Acesso à internet para comunicação com a API da AWS

## Instalação

Siga os passos abaixo para configurar o ambiente:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/analisador-links-suspeitos.git
   cd analisador-links-suspeitos
   ```

2. Crie um ambiente virtual Python:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install boto3
   pip install langchain
   ```

## Configuração das Credenciais AWS

Para configurar corretamente o acesso ao AWS Bedrock, siga estas etapas:

### Método 1: Usando o AWS CLI

1. Instale o AWS CLI seguindo as [instruções oficiais](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

2. Configure suas credenciais:
   ```bash
   aws configure
   ```

3. Insira suas credenciais quando solicitado:
   ```
   AWS Access Key ID: [SUA_ACCESS_KEY]
   AWS Secret Access Key: [SUA_SECRET_KEY]
   Default region name: us-east-1
   Default output format: json
   ```

### Método 2: Configuração Manual

1. Crie ou edite o arquivo `~/.aws/credentials` (Linux/Mac) ou `C:\Users\USERNAME\.aws\credentials` (Windows):
   ```
   [default]
   aws_access_key_id = SUA_ACCESS_KEY
   aws_secret_access_key = SUA_SECRET_KEY
   ```

2. Crie ou edite o arquivo `~/.aws/config` (Linux/Mac) ou `C:\Users\USERNAME\.aws\config` (Windows):
   ```
   [default]
   region = us-east-1
   output = json
   ```

### Método 3: Variáveis de Ambiente

Defina as seguintes variáveis de ambiente:

```bash
# Linux/Mac
export AWS_ACCESS_KEY_ID=SUA_ACCESS_KEY
export AWS_SECRET_ACCESS_KEY=SUA_SECRET_KEY
export AWS_DEFAULT_REGION=us-east-1

# Windows (PowerShell)
$env:AWS_ACCESS_KEY_ID="SUA_ACCESS_KEY"
$env:AWS_SECRET_ACCESS_KEY="SUA_SECRET_KEY"
$env:AWS_DEFAULT_REGION="us-east-1"
```

### Verificação de Acesso ao Bedrock

Para verificar se suas credenciais estão configuradas corretamente, execute:

```python
import boto3

try:
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1'
    )
    # Teste simples para verificar acesso
    models = bedrock.list_foundation_models()
    print("Conexão com AWS Bedrock estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar com AWS Bedrock: {e}")
```

## Uso

Para utilizar o analisador de links suspeitos, siga estas instruções:

1. Execute o script:
   ```bash
   python analisar_links.py
   ```

2. O sistema analisará cada URL da lista e fornecerá:
   - Avaliação de suspeita com justificativa
   - Recomendação sobre quem deve ser notificado
   - Um modelo de e-mail formal para comunicar a ameaça

## Personalização

### Modificando a Lista de URLs

Para analisar diferentes URLs, modifique a lista `urls` no código:

```python
urls = [
    "https://seu-link-suspeito-1.com",
    "https://seu-link-suspeito-2.com",
    # Adicione mais URLs conforme necessário
]
```

### Ajustando o Prompt

O template de prompt pode ser modificado para extrair diferentes tipos de informações:

```python
prompt_template = """
Você é um analista de cibersegurança que responde somente na língua português brasileiro. Para o link abaixo, forneça:

1. Identificação: O link é suspeito? Por quê?
2. Classificação: Qual o tipo de ameaça (phishing, malware, etc)?
3. Nível de risco: Baixo, Médio ou Alto?
4. Notificação: Quem deve ser notificado?
5. Mensagem: Gere um e-mail formal sobre a ameaça.

Link: {url}
"""
```

### Ajustando Parâmetros do Modelo

Os parâmetros do modelo podem ser ajustados para controlar o comportamento da geração:

```python
body=json.dumps({
    "prompt": prompt,
    "max_tokens": 512,     # Aumentar para respostas mais longas
    "temperature": 0.2,    # Aumentar para mais criatividade, diminuir para mais consistência
    "top_p": 0.9           # Controla a diversidade das respostas
})
```

## Considerações Técnicas

### Formato de URLs

O código utiliza a notação `[.]` em alguns domínios para evitar cliques acidentais em links maliciosos durante a análise do código. Esta é uma prática comum em análise de segurança.

### Limitações do Modelo

- O modelo Mistral-7B pode não identificar corretamente 100% das ameaças
- A análise é baseada em padrões aprendidos durante o treinamento do modelo
- Recomenda-se usar esta ferramenta como um primeiro passo de triagem, não como substituto para análise humana especializada

### Custos de Uso

O uso do AWS Bedrock incorre em custos baseados no volume de tokens processados. Consulte a [página de preços do AWS Bedrock](https://aws.amazon.com/bedrock/pricing/) para informações atualizadas.

## Segurança

Este código deve ser executado em ambiente seguro, pois:
1. Manipula URLs potencialmente maliciosos
2. Utiliza credenciais AWS que devem ser protegidas
3. Pode gerar informações sensíveis sobre vulnerabilidades

## Contribuições

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Contato

Para questões ou sugestões, entre em contato através de [lorenzo.matheo@hotmail.com].
