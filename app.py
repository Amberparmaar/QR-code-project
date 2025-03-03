import qrcode
img = qrcode.make('https://q2-nextjs-blog-oq7h.vercel.app/')
print(type(img))
img.save('AP Coffee Blog.png')
print('QR Code Generated!')
