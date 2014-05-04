System Requirements
###################

:slug: requirements


.. raw:: html
    
    <script type="text/javascript">
    $(function() {
        var id = normalisePlatform()[0];
        if (id == null)
            id = "windows";
        $('#platformtabs a[href="#' + id + '"]').tab('show');
        $('.archinfo').addClass('b' + arch);
    });
    function switchtabs(id) {
        $('#platformtabs a[href="#' + id + '"]').tab('show');
    };
    </script>

    <div class="tabbable archinfo">
        <ul class="nav nav-tabs" id="platformtabs">
            <li><a href="#linux" data-toggle="tab"><i class="fa fa-linux"></i> GNU/Linux</a></li>
            <li class="active"><a href="#windows" data-toggle="tab"><i class="fa fa-windows"></i> Windows</a></li>
            <li><a href="#mac" data-toggle="tab"><i class="fa fa-apple"></i> Mac OS X (beta)</a></li>
        </ul>

        <div class="tab-content">
            <div class="tab-pane" id="linux">
                <p>If you have a recent desktop or laptop computer, then <em>S. Cargo</em> should work on it.
                <em>S. Cargo</em> runs well on Ubuntu 13.04 computers manufactured since 2011. Minimum Specifications:</p>

                <ul class="simple">
                    <li><i class="fa fa-bolt fa-fw"></i> <strong>CPU:</strong> i686 and x86_64 processors are supported. These processors are common in desktop and laptop computers. Your CPU must be at least as fast as the <a class="reference external" href="http://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+i5+U+430+%40+1.20GHz&amp;id=783">Intel Core i5 U430</a>. ARM CPUs (which are common in mobile devices such as tablets) are not supported.</li>
                    <li><i class="fa fa-desktop fa-fw"></i> <strong>Video:</strong> Intel, nVidia and AMD video cards are supported. Your video card must support OpenGL 4 and be at least as fast as the <a class="reference external" href="http://www.videocardbenchmark.net/gpu.php?gpu=Mobility+Radeon+HD+5430&amp;id=515">AMD Mobility Radeon HD 5430</a>. For some cards, you may need to use proprietary video drivers (i.e. those provided by the video card manufacturer) to get the required graphics performance. Sorry about that.</li>
                </ul>
            </div>

            <div class="tab-pane" id="windows">
                <p>If you have a recent desktop or laptop computer, then <em>S. Cargo</em> should work on it.
                <em>S. Cargo</em> runs well on Windows 7 computers manufactured since 2011. Minimum Specifications:</p>

                <ul class="simple">
                    <li><i class="fa fa-bolt fa-fw"></i> <strong>CPU:</strong> i686 and x86_64 processors are supported. These processors are common in desktop and laptop computers. Your CPU must be at least as fast as the <a class="reference external" href="http://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+i5+U+430+%40+1.20GHz&amp;id=783">Intel Core i5 U430</a>. ARM CPUs (which are common in mobile devices such as tablets) are not supported.</li>
                    <li><i class="fa fa-desktop fa-fw"></i> <strong>Video:</strong> Intel, nVidia and AMD video cards are supported. Your video card must support OpenGL 4 and be at least as fast as the <a class="reference external" href="http://www.videocardbenchmark.net/gpu.php?gpu=Mobility+Radeon+HD+5430&amp;id=515">AMD Mobility Radeon HD 5430</a>.</li>
                </ul>
            </div>

            <div class="tab-pane" id="mac">
                <p><em>S. Cargo</em> runs well on the Macbook Pro with Retina (2.5 GHz I5 and 8GB Ram) and the Mac Mini (2.5 GHz I5 4GB Ram).</p>

                <ul class="simple">
                    <li><i class="fa fa-bolt fa-fw"></i> <strong>CPU:</strong> i686 and x86_64 processors are supported. These processors are common in desktop and laptop computers. Your CPU must be at least as fast as the <a class="reference external" href="http://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+i5+U+430+%40+1.20GHz&amp;id=783">Intel Core i5 U430</a>. ARM CPUs (which are common in mobile devices such as tablets) are not supported.</li>
                    <li><i class="fa fa-desktop fa-fw"></i> <strong>Video:</strong> Unknown.</li>
                </ul>

                <p><i class="fa fa-exclamation-triangle fa-fw"></i> This is a <a class="reference external" href="http://en.wikipedia.org/wiki/Software_release_life_cycle#Beta">beta release</a> of S. Cargo for <strong>64-bit Mac OS X 10.6+</strong>. It's fully playable, but it <a class="reference external" href="https://github.com/oasakfu/cargo/issues/2">might be slow on some computers</a>. If you buy S. Cargo for OS X and find that it doesn't play well on your computer, you can:</p>

                <ul class="simple">
                    <li>Try running it in a Windows virtual machine e.g. using Parallels.</li>
                    <li><a class="reference external" href="https://github.com/oasakfu/cargo#s-cargo">Download the source code</a> and play the game in Blender.</li>
                    <li>Ask us for a refund.</li>
                </ul>

                <p>Any feedback about this would be appreciated. Please let us know whether it runs well for you, and what kind of Apple computer you have. You can leave a comment in the <a class="reference external" href="https://github.com/oasakfu/cargo/issues/2">issue tracker</a> or tweet to <a class="reference external" href="https://twitter.com/asmidgin">&#64;asmidgin</a>.</p>
            </div>
        </div>

    </div>

    <p>See also:</p>
    <ul>
        <li><a href="#linux" onclick="switchtabs('linux')"><i class="fa fa-linux fa-fw"></i> GNU/Linux</a></li>
        <li><a href="#windows" onclick="switchtabs('windows')"><i class="fa fa-windows fa-fw"></i> Windows</a></li>
        <li><a href="#mac" onclick="switchtabs('mac')"><i class="fa fa-apple fa-fw"></i> Mac OS X</a></li>
    </ul>

