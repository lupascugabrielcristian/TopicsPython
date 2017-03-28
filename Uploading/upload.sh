cp ../*.json ./
zip allData.zip *.json
rm ./*.json
restdb-cli --cmd upload --src allData.zip --dest ./ --database Topics-E26e --apikey 8a598b90e251b3edaed8860761b4852a5cbd1
rm allData.zip