from bing_image_downloader import downloader #pip install bing-image-downloader


keywords = [
    "architectural facade",
    "modern building facade",
    "parametric facade architecture",
    "computational facade design"
]

for kw in keywords:
    downloader.download(
        kw,
        limit=50,
        output_dir="dataset_raw",
        adult_filter_off=True,
        force_replace=False,
        timeout=60
    )
###############################################
# bing image downloader ile görsel indirdik.
# Blip ile txt dosyalarını oluşturacağız ki bu tasvirler loRA için çok önemli olacak.
###############################################

###############################################
# aşağıdaki yöntem burada işe yaramadı çünkü bu yöntem YOLO iin boxable nesne oluşturuyor ,bizim işimiz görmeyecek biz sadece label arıyoruz éFacadeé labelı burada yok
###############################################

#open images ile  kendi datasetini oluşturabilirsin: https://storage.googleapis.com/openimages/web/visualizer/index.html?type=all&set=train&c=%2Fm%2F01x314
#https://www.youtube.com/watch?v=SjsF8_kDigw bu youtube videosunda nasıl yapıldığını bulabilirsin
#indrime toolkiti'i https://github.com/theAIGuysCode/OIDv4_ToolKit