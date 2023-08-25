from libs.using_ffm import get_ffm, get_embed


mstr = "請幫我寫一篇 '感謝使用 TWCC AI 算力雲端服務' 的客服信件，並附上客服 email: service@twsc.io"

embed = get_embed()
print("Testing AFS Cloud Embedding Service:")
print(embed.embed_documents([mstr])[0][:3])

print("Testing AFS Cloud FFM Service:")
ffm = get_ffm()
print(ffm.predict(mstr))
