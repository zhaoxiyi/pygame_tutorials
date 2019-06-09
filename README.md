# pygame_tutorials
Fork from kidscancode
Code to go along with lessons at http://kidscancode.org/lessons

# 本项目为了儿子对自己完成一个Python game的期望而建
For my son. He want to build a Python game by him self. So here is the tutorials

第一课前的准备知识： 
Python是什么，Python是一种程序语言，计算机的世界里还有很多种语言，有java，有go，你玩的 Roblox 使用的是 Lua 语言。 你的iPad里有很多种语言同时存在。iPad上的Roblox还是Lua，iPad里的我的世界同时使用了 Python和C++。所以程序语言只是为了你写程序方便，电脑或者iPad在运行的时候会把你写的程序语言翻译成它们喜欢的形式，一种被翻译过适合它自己CPU的“编译语言”。每一种CPU都有自己的“习惯短语”，那就是它们的“指令集”，所以不同CPU在工作的时候是不太一样的，主要的原因是为了它们工作效率更高在使用预先给它们设计好的”习惯短语“指令集。

VSCode是什么，爸爸把你的电脑安装好了VSCode，你打开VSCode就能看到你现在用来写程序的窗口。但VSCode并不是你的程序，它只是为了让你写程序的时候不用自己做太多其它准备而设计的”编程工具“。有了它你即使不太懂得你在哪里写程序，或者不太记得程序应该怎样写，“编程工具” VSCode也能尽量帮助你完成和改正你的程序。这样你可以更容易完成你希望写程序的目标，换句话说，其实没有VSCode你也可以写程序的，就像有时候爸爸临时写程序时候那样，但是完整的完成一个程序当然是像VSCode这样的工具更加方便，因为他有很多功能可用，我会在咱们的课程里包含一些常用的功能。比如第一个需要知道的信息就是，如果你需要在新的VSCode里写程序，你就需要重新找到你原来的程序所在的目录，或是新建一个目录作为你的程序基础目录。先在中间的 workspace 窗口上选择一个基础目录，选在哪里都可以，它将是你未来存储代码的位置。然后到最上面的菜单中找到 Terminal这个菜单，在里面选择 “Run Task...." 这个命令。最后在跳出来的命令框里面贴下这句话 “git clone https://github.com/zhaoxiyi/pygame_tutorials.git" 然后“回车”，回车还记得么，最右边那个最大的有向回箭头的那个按钮。等到下面窗口的过程全部运行完成就可以看到我给你准备好的教程和你之前已经写过的所有代码了。

Git是什么，上面用到的git clone命令是为了将你和我的代码从网络上拿回来。因为我把咱们的代码放到了一个叫“Github”的地方。Github.com 这个网站你可以直接在浏览器上访问哦,在浏览器上也可以看到你写的代码。最酷的是，这里是全世界最酷的开发人员一起写代码的地方。因为全世界的程序员都把自己最酷的想法和程序放在这里，大家都可以看到这些“源程序代码”，所以我们叫“开源”，也叫“代码开源”。我们用的基础程序是爸爸从一个叫 kidscancode 的网站fork过来的，就像扫描仪一样，fork一下我们的git账户下也有了这个程序。现在我和你一起把程序也放在这里，所以我们两个也是“开源程序员”了。也就是说你也是全球开源程序员之中的一员了，如果你在这里写的练习程序可以帮助到其它的小朋友，那么你也为全世界的开源计划做出了自己的贡献，这是不是很酷？超酷？超级supper酷？你也可以把你做的事情告诉你的同学，让他们来学习，告诉你学校的老师让他可以用这个项目教更多的小朋友。这就是开源最酷的地方，他能让你更酷更了不起。

README.md 是什么， 每个Github上的项目都会默认给别人看这个“README.md”的文件。 所以你如果从 Github 上查找这个pygame项目的时候，第一个给人看到的说明就是这个“README.md”里面所写的内容。所以我把给你写的教程就写在这里面。而且每个目录里也可以使用这样的文件来解释目录下面放了一些什么内容。未来你对这个课程里面的内容有什么看得懂或者看不懂的内容都可以写在这里，我们一起给他家展示一个10岁小朋友想要写一个游戏程序的时候，什么是需要了解的，什么是自己可以理解的，什么是需要帮助的。

Branch 是什么，在Github上可以建立一种叫 branch 的分支程序。我们现在用的是master 也就是主要分支，将来咱们一起完成的内容就都回合并的主分支里给大家看。 同时我为你建立了一个叫 “son” 的branch 分支。你自己写的内容要放到这个分支中。你使用 VSCode 里面分支图标按钮里，点击 pygame_tutorials 后面属于这个程序的分支小图标，就会看到有master，有son，还有+号，你点击 son 就会转向专门属于你的分支。你有什么想说的，你的练习都可以写到这个分支里。当我看到你的分支，我就会知道你在家做了什么，无论我在哪里都可以看到你的问题和你的进步。我会再做一个father分支，在father分支里面只会加入我还没有完善的内容，你可以来看我还未为你准备完成的练习和讲解。我们的工作内容最终都可以合并到master分支里，变成一个完整的内容。

## [第一课：建立一个游戏基础场景模版] (./firstclass.md)



