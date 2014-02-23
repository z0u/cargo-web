var normalisePlatform = function() {
    var os;
    var arch;
    var platform = window.navigator.platform;
    var ua = window.navigator.userAgent;

    if (/linux/i.exec(platform) !== null)
        os = 'linux';
    else if (/mac/i.exec(platform) !== null)
        os = 'mac';
    else if (/win/i.exec(platform) !== null)
        os = 'windows';
    else
        os = null;

    if (/x86_64|x86-64|Win64|x64;|amd64|WOW64|x64_64/i.exec(ua) !== null)
        arch = "64";
    else
        arch = "32";

    return [os, arch];
};
