curl -O https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json

grep -o '"version":"[^"]*"' last-known-good-versions.json | head -1 | cut -d'"' -f4 > chrome_version.txt

stableVersion=$(cat chrome_version.txt)

#curl -O "https://storage.googleapis.com/chrome-for-testing-public/$stableVersion/linux64/chrome-linux64.zip"
#unzip chrome-linux64.zip

curl -O "https://storage.googleapis.com/chrome-for-testing-public/$stableVersion/linux64/chromedriver-linux64.zip"
unzip chromedriver-linux64.zip

mkdir chromedriver

cp chromedriver-linux64/chromedriver chromedriver/