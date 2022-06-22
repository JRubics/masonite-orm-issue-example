# Example for masoniteorm issue: `QueryBuilder created with new_from_builder() use the same references as the builder it is created from #682`

### Run database
```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest
```

### Create and enter venv
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run migrations
```
masonite-orm migrate -d migrations
```

### Run example:
```
python main.py
```

NOTE: `requirements.txt` contains the version before fix (`2.13.2`). Try the same with `masonite-orm==2.13.3` - it shows that the fix doesn't work properly