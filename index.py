#!/usr/bin/env python

import web
import os, errno

urls = (
    '/', 'index'
)

_index = 0;


class index:
    def GET(self):
        return 'I\'m ready for that, you know.'

    def POST(self):
        i = web.input()
        path = i.to;
        if os.path.isfile(path):
            os.remove(path);
            print path + ' del!';
        else:
            print path + 'not exist!';

        _dir = os.path.dirname(os.path.abspath(path));
        if os.path.exists(_dir) == False:
            self.mkdir_p(_dir)
            print 'create dir:' + _dir;

        fout = open(path, 'w')
        fout.write(i.file)
        fout.close()
        # print 'pos-receive:' + i.to;
        return 200


    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise


class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


if __name__ == '__main__':
    app = MyApplication(urls, globals())
    app.run(port=8991)
