fetchProduct(productUrl: string) {
  if (!productUrl) return;
  
  const apiUrl = "http://127.0.0.1:5000/fetch_ali_details";
  this.http.post(apiUrl, { url: productUrl }).subscribe((res: any) => {
    if (res.ok) {
      this.currentProduct = {
        title: res.title,
        image: res.image,
        url: res.url,
        price: "تحليل السعر الكوني..." // سيتم تحديثه عند جلب السعر
      };
    }
  });
}
