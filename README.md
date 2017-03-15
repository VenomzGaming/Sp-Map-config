# Sp-Map-config
A Sourcepython plugin which allow you to configure Cvar and restriction by map.

<h2>How to install it ?</h2>

Put the plugin in <b>addons/source-python/plugins</b> directory.<br>
Go in <b>cfg/source-python</b> directory and add a folder <b>map_config</b>. In this folder you can add maps configs.

<h2>How to use it ?</h2>

<h4>Restriction system :</h4>

I made my restriction like this :
> restrict_ + weapon name + _team <br>
1 - Weapon is restricted<br>
0 - Weapon not restricted

- Default :<br>
You can find a map_config.cfg in <b>cfg/source-python</b> directory. It's the default config always load before map config. In this file you can just set restriction. If you want on all of your maps add a restriction on Awp you can do this in this file.

- By map :
>Example :<br><br>
// File de_dust2.cfg<br>
restrict_ssg08_t 1<br>
restrict_ssg08_ct 1

With this config when you are on de_dust2 ssg08 will be restricted for CT and T.

<h4>Cvar system :</h4>

>Example :<br><br>
// File de_dust2.cfg<br>
sv_alltalk 0

You can also add cvar in the config file, in our example when you are on de_dust2 alltalk cvar will be set to 0.

