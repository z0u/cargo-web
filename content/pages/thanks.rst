Thanks
######

:slug: thanks
:status: hidden

.. role:: btn

Thanks for purchasing Cargo. We hope you enjoy playing!


.. raw:: html
    
    <script type="text/javascript">
    $(function() {
        var id = normalisePlatform()[0];
        if (id == null)
            id = "windows";
        $('#platformtabs a[href="#' + id + '"]').tab('show');

        var platforms = ['linux', 'windows'];
        var arch = normalisePlatform()[1];
        for (var i = 0; i < platforms.length; i++) {
            var platform = platforms[i];
            var btnselector = '#' + platform + ' .b' + arch;
            $('#' + platform + ' .btn-main-download')
                .attr('href', $(btnselector).first().attr('href'));
        }
        $('.architecture').text(arch)
    });
    function switchtabs(id) {
        $('#platformtabs a[href="#' + id + '"]').tab('show');
    };
    </script>

    <div class="tabbable">
        <ul class="nav nav-tabs" id="platformtabs">
            <li><a href="#linux" data-toggle="tab">GNU/Linux</a></li>
            <li class="active"><a href="#windows" data-toggle="tab">Windows</a></li>
            <li><a href="#mac" data-toggle="tab">Mac OS X</a></li>
            <li><a href="#source" data-toggle="tab">Source Code</a></li>
        </ul>
        <div class="tab-content">
            <div class="tab-pane" id="linux">
                <p class="text-center">
                    <a href="#" class="btn btn-primary btn-large btn-main-download">Download S. Cargo for GNU/Linux <span class="architecture"></span>-bit</a>
                </p>

                <p>Instructions:</p>

                <ol>
                    <li>Download the file.</li>
                    <li>Double-click on it to open the archive.</li>
                    <li>Copy the <em>cargo-1.02</em> folder from the archive to your desktop, e.g. by dragging-and-dropping it.</li>
                    <li>Close the archive-viewing utility.</li>
                    <li>Open the <em>cargo-1.02</em> folder on your desktop.</li>
                    <li>Double-click on <em>cargo</em> to start the game.</li>
                    <li>Play it!</li>
                    <li>Press F11 at any time to quit.</li>
                </ol>

                <p>Additional instructions are available in the file <em>readme.html</em> (inside the archive).</p>

                <h3>Alternative Downloads</h3>
                <p>It looks like you are using a <span class="architecture"></span>-bit operating system. If you are unsure, <a href="http://stackoverflow.com/questions/246007/how-to-determine-whether-a-given-linux-is-32-bit-or-64-bit">this site has information about how to find out</a>. There are <a href="http://askubuntu.com/a/65731/81211">special instructions</a> for Ubuntu.</p>

                <ul>
                <li><a href="https://drive.google.com/uc?id=0B9ifjT3w1yFSc2FxRVhBclhsTDg&export=download" class="b64 btn-download" title="For x86_64 CPUs running GNU/Linux">
                    Download the 64-bit version from Google Drive
                </a></li>
                <li><a href="https://drive.google.com/uc?id=0B9ifjT3w1yFSRjFJNDVJcXY3cTg&export=download" class="b32 btn-download" title="For i686 CPUs running GNU/Linux">
                    Download the 32-bit version from Google Drive
                </a></li>
                <li><a href="/static/releases/cargo-1.02-gnu+linux-64.tar.bz2" class="b64 btn-download" title="For x86_64 CPUs running GNU/Linux">
                    Download the 64-bit version from Smidgin
                </a></li>
                <li><a href="/static/releases/cargo-1.02-gnu+linux-32.tar.bz2" class="b32 btn-download" title="For i686 CPUs running GNU/Linux">
                    Download the 32-bit version from Smidgin
                </a></li>
                </ul>
            </div>

            <div class="tab-pane active" id="windows">
                <p class="text-center">
                    <a href="#" class="btn btn-primary btn-large btn-main-download">Download S. Cargo for Windows <span class="architecture"></span>-bit</a>
                </p>

                <p>Instructions:</p>

                <ol>
                    <li>Download the file.</li>
                    <li>Double-click on it to open the archive.</li>
                    <li>Copy the <em>cargo-1.02</em> folder from the archive to your desktop, e.g. by dragging-and-dropping it.</li>
                    <li>Close the archive-viewing utility.</li>
                    <li>Open the <em>cargo-1.02</em> folder on your desktop.</li>
                    <li>Double-click on <em>cargo.exe</em> to start the game. For some users, this file will simply be called "<em>cargo</em>".</li>
                    <li>Play it!</li>
                    <li>Press F11 at any time to quit.</li>
                </ol>

                <p>Additional instructions are available in the file <em>readme.html</em> (inside the archive).</p>

                <h3>Alternative Downloads</h3>
                <p>It looks like you are using a <span class="architecture"></span>-bit operating system. If you are unsure, please check <a href="http://support.microsoft.com/kb/827218">Microsoft's support site</a>.</p>

                <ul>
                <li><a href="https://drive.google.com/uc?id=0B9ifjT3w1yFSaXJqOVl4RUVaSVk&export=download" class="b64 btn-download" title="For x86_64 CPUs running Windows">
                    Download the 64-bit version from Google Drive
                </a></li>
                <li><a href="https://drive.google.com/uc?id=0B9ifjT3w1yFSdlZLLVlDZGFkcXc&export=download" class="b32 btn-download" title="For i686 CPUs running Windows">
                    Download the 32-bit version from Google Drive
                </a></li>
                <li><a href="/static/releases/cargo-1.02-windows-64.zip" class="b64 btn-download" title="For x86_64 CPUs running Windows">
                    Download the 64-bit version from Smidgin
                </a></li>
                <li><a href="/static/releases/cargo-1.02-windows-32.zip" class="b32 btn-download" title="For i686 CPUs running Windows">
                    Download the 32-bit version from Smidgin
                </a></li>
                </ul>
            </div>

            <div class="tab-pane" id="mac">
                <p>Sorry, S. Cargo is not currently available for OS X. Please see <a href="/pages/requirements.html">system requirements</a>.</p>

                <p>If you download <a href="#source" onclick="switchtabs('source')">the source</a>, you can play the game by opening <em>game/cargo.blend</em> in <a href="http://blender.org/download">Blender</a> (instead of running the <em>cargo</em> executable). This should work well on all platforms that Blender runs on, including OS X. However the experience won't be as good as running the pre-built game: it is more complicated and it won't run in full-screen mode.</p>
            </div>

            <div class="tab-pane" id="source">
                <p>The source code for S. Cargo is available in <a href="https://github.com/oasakfu/cargo">a git repository</a>.</p>
            </div>
        </div>
    </div>
