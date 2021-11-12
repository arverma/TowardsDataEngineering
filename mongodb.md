To have launchd start mongodb/brew/mongodb-community now and restart at login:

  `brew services start mongodb/brew/mongodb-community`
  
Or, if you don't want/need a background service you can just run:

  `mongod --config /opt/homebrew/etc/mongod.conf`
