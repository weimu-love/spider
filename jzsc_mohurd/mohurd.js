let CryptoJs = require('crypto-js');

p = CryptoJs.enc.Utf8.parse("jo8j9wGw%6HbxfFn");
f = CryptoJs.enc.Utf8.parse("0123456789ABCDEF");

function getData(t) {
    var e = CryptoJs.enc.Hex.parse(t),
        n = CryptoJs.enc.Base64.stringify(e),
        a = CryptoJs.AES.decrypt(n, p, {
            iv: f,
            mode: CryptoJs.mode.CBC,
            padding: CryptoJs.pad.Pkcs7
        }),
        i = a.toString(CryptoJs.enc.Utf8);
    return i.toString()
}
