# simple_dvc_server
Bare-bones server which supports will serve as a file backend to DVC 

# Installation
`pip install simple-dvc-server`

# Running
Backend
```
cd your_backing_store_dir
simple-dvc-server
```
You can also set the backing store dir arbitrarily with `-w/--workdir`. 

In your repo:
```
dvc remote add --default myremote http://localhost:4223/some/path
dvc push
```
 This will store files at your_backing_store_dir/some/path/OBJECT, where `OBJECT` is `ab/cdef123456`, with the first two letters of the hash as the prefix dir (typical git object dir notation) 

### Note

You may have to fiddle with your `--host` flag depending on your envirnoment/container status/etc. `'':4223`, `localhost:4223`, and `0.0.0.0:4223` all have different semantics. See [http.server](https://docs.python.org/3/library/http.server.html) for more details. 
