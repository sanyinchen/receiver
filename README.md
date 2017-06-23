# receiver

### Describe

This is a receiver of fis3 in python.

### Usage

+ Make sure you have env of python
+ ``` git clone https://github.com/sanyinchen/receiver.git ```
+ cd receiver
+ python index.py

### Fis3 Deploy Configuration

	fis.match('*', {
   		 deploy: fis.plugin('http-push', {
        receiver: 'http://<your host>:8991',
        to: '/Users/yinchensan/demo/temp' // the path is you remote machine  
      })
	})
