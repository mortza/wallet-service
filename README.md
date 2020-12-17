# Wallet Service
این سیستم برای مدیریت تراکنش های مالی ساخته شده است که دارای توابع زیر می باشد که در رابطه با هرکدام به تفضیل توضیح داده می شود.

## Wallet Transaction 
این تابع یک تراکنش مالی را ثبت می کند و در جیب متناسب با کیف پول کاربر مورد نظر قرار می گیرد مسیر دسترسی آن و ورودی ها و خروجی این تابع به صورت زیر تعریف می شود.

```
OPTIONS /wallet/wallet/transaction/new/
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet Transaction Create Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "date": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Date"
            },
            "amount": {
                "type": "float",
                "required": true,
                "read_only": false,
                "label": "Amount"
            },
            "transaction_information": {
                "type": "field",
                "required": false,
                "read_only": false,
                "label": "Transaction information"
            },
            "wallet": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Wallet"
            }
        }
    }
}
```
## Get Wallet Transaction List
این تابع لیست تمام تراکنش های مربوط به کیف پول ها را بر می گرداند.


```
OPTIONS /wallet/wallet/transaction/list/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet Transaction List Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Get Wallet Transaction Details
با استفاده از این تابع می توانیم به جزئیات اطلاعات هر تراکنش دسترسی داشته باشیم.این عملیات با ارسال آیدی مربوط به تراکنش انجام می شود.
```
iOPTIONS /wallet/wallet/transaction/<transaction_id>/detail/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet Transaction Retrieve Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Create Wallet
این تابع برای ساختن یک کیف پول با جیب های مختلف برای کار می باشد. به این صورت که از این تابع استفاده کرده و مقدار یوزر آیدی و نام جیب مورد نظر را به تابع می دهیم تا کیف پول و جیب هایش را برایمان بسازد.
```
OPTIONS /wallet/wallet/new/
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet Create Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "user_id": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "User id"
            },
            "pocket_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Pocket name",
                "max_length": 128
            },
            "balance": {
                "type": "float",
                "required": false,
                "read_only": true,
                "label": "Balance"
            },
            "is_block": {
                "type": "boolean",
                "required": false,
                "read_only": true,
                "label": "Is block"
            }
        }
    }
}
```
## Get Wallet List
این تابع برای دریافت لیست تمام کیف پول ها استفاده می شود.

```
OPTIONS /wallet/wallet/list/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet List Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Get Wallet Details
از این تابع برای دریافت جزئیات اطلاعات کیف پول ها استفاده می شود.
```
OPTIONS /wallet/wallet/<wallet_id>/detail/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet Retrieve Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Block Wallet Or Unblock Wallet
از این تابع برای بلاک کردن یا فعال کردن کیف پول استفاده می شود.
```
OPTIONS /wallet/wallet/<wallet_id>/update/
HTTP 200 OK
Allow: GET, PUT, PATCH, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Wallet Retrieve Update Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "PUT": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "user_id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "User id"
            },
            "pocket_name": {
                "type": "string",
                "required": false,
                "read_only": true,
                "label": "Pocket name"
            },
            "balance": {
                "type": "float",
                "required": false,
                "read_only": true,
                "label": "Balance"
            },
            "is_block": {
                "type": "boolean",
                "required": true,
                "read_only": false,
                "label": "Is block"
            }
        }
    }
}
```
## Your Pocket Transaction
این تابع برای دریافت تراکنش های مربوط به 'جیب تو' ساخته شده است و تراکنش های مربوط را ثبت و تغیرات را اعمال می نماید.

```
OPTIONS /wallet/your-pocket/transaction/new/
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Your Pocket Transaction Create Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "date": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Date"
            },
            "amount": {
                "type": "float",
                "required": true,
                "read_only": false,
                "label": "Amount"
            },
            "transaction_information": {
                "type": "field",
                "required": false,
                "read_only": false,
                "label": "Transaction information"
            },
            "your_pocket": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Your pocket"
            }
        }
    }
}
```
## Get Your Pocket Transaction List
این تابع برای دریافت لیست تمام تراکنش های مربوط به جیب تو ها استفاده می شود.
```
OPTIONS /wallet/your-pocket/transaction/list/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Your Pocket Transaction List Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Get Your Pocket Transaction Details
این تابع برای دریافت جزئیات مربوط به تراکنش های جیب تو استفاده می شود.
```
OPTIONS /wallet/your-pocket/transaction/<transaction_id>/detail/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Your Pocket Transaction Retrieve Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Create Your Pocket
این تابع برای ساخت جیب تو استفاده می شود. به این صورت که یک یوزر آدی دریافت می کند و در صورتی که جیب تو ی فعالی برای کاربر مورد نظر موجود نباشد یک جیب تو برای آن می سازد و زمان فعال بودن آن را تا سی روز دیگر مشخص می کند.

```
OPTIONS /wallet/your-pocket/new/
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Your Pocket Create Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "id": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "user_id": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "User id"
            },
            "balance": {
                "type": "float",
                "required": false,
                "read_only": true,
                "label": "Balance"
            },
            "active": {
                "type": "boolean",
                "required": false,
                "read_only": true,
                "label": "Active"
            },
            "expiry_date": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Expiry date"
            },
            "your_pocket_information": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Your pocket information"
            }
        }
    }
}
```
## Get Your Pocket List
این تابع لیست تمام جیب تو های فعال را بر میگرداند.
```
OPTIONS /wallet/your-pocket/list/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Your Pocket List Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```
## Get Your Pocket Details
این تابع جزئیات اطلاعات مربوط به جیب تو را بر میگرداند.
```
OPTIONS /wallet/your-pocket/<your_pocket_id>/detail/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Your Pocket Retrieve Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```

## Get All Transaction
این تابع لیست تمام تراکنش های موجود را بر میگرداند.
```
OPTIONS /wallet/all/transaction/list/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "All Transaction List Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```

## Get Transaction Details
این تابع ریز اطلاعات مربوط به هر تراکنش را برمگرداند.

```
OPTIONS /wallet/all/transaction/<transaction_id>/detail/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "All Transaction Retrieve Api",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ]
}
```