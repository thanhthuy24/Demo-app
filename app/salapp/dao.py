def load_categories():
    return [{
        'id' : 1,
        'name' : 'Mobile'
    },
        {
            'id': 2,
            'name': 'Laptop'
    }]

def load_products(kw = None):
    products = [{
        'id' : 1,
        'name' : 'iPhone 13',
        'price' : 20000000,
        'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
    },
        {
            'id': 2,
            'name': 'galaxy s22',
            'price': 20000000,
            'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
        },
        {
            'id': 3,
            'name': 'iPhone 13',
            'price': 20000000,
            'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
        },
        {
            'id': 3,
            'name': 'iPhone 13',
            'price': 20000000,
            'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
        },
        {
            'id': 3,
            'name': 'iPhone 13',
            'price': 20000000,
            'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
        },{
            'id': 3,
            'name': 'iPhone 13',
            'price': 20000000,
            'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
        },
        {
            'id': 3,
            'name': 'iPhone 13',
            'price': 20000000,
            'image': 'https://trangthienlong.com.vn/wp-content/uploads/2022/10/iphone-13-mau-hong-pink-128gb-256gb-512gb-trang-thien-long-mobile-510x510.jpg'
        }
    ]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products