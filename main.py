import g4f
import asyncio

_providers = [
    # g4f.Provider.AItianhuSpace,
    # g4f.Provider.AiChatOnline,
    #g4f.Provider.Aura,
    # g4f.Provider.Bard,
    # g4f.Provider.Bing,
    #g4f.Provider.ChatBase,
    # g4f.Provider.ChatForAi,
    # g4f.Provider.ChatgptAi,
    # g4f.Provider.ChatgptDemo,
    # g4f.Provider.ChatgptNext,
    # g4f.Provider.Chatxyz,
    #g4f.Provider.DeepInfra,
    # g4f.Provider.FreeChatgpt,
    # g4f.Provider.GPTalk,
    # g4f.Provider.GeminiProChat,
    # g4f.Provider.Gpt6,
    # g4f.Provider.GptChatly,
    # g4f.Provider.GptForLove,
    # g4f.Provider.GptGo,
    # g4f.Provider.GptTalkRu,
    # g4f.Provider.Hashnode,
    #g4f.Provider.HuggingChat,
    # g4f.Provider.Koala,
    # g4f.Provider.Liaobots,
    # g4f.Provider.Llama2,
    # g4f.Provider.MyShell,
    # g4f.Provider.OnlineGpt,
    # g4f.Provider.OpenaiChat,
    # g4f.Provider.PerplexityAi,
    # g4f.Provider.PerplexityLabs,
    # g4f.Provider.Phind,
    #g4f.Provider.Pi,
    # g4f.Provider.Poe,
    # g4f.Provider.Raycast,
    # g4f.Provider.TalkAi,
    # g4f.Provider.Theb,
    # g4f.Provider.ThebApi,
    # g4f.Provider.Yqcloud,
]


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Кто ты такой?"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)


asyncio.run(run_all())
