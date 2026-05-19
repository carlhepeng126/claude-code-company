$d = (Get-Date -Format "yyyyMMdd")
$o = "C:\Users\Admin\Documents\LLM Wiki\收件箱：同步助手\本地采集\$d"
$env:Path = "C:\Program Files\nodejs;C:\Users\Admin\AppData\Roaming\npm;" + $env:Path
New-Item -ItemType Directory -Path $o -Force | Out-Null

# 小红书 (5个关键词)
try { $r = opencli xiaohongshu search "企业英语培训" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\xhs-english.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ xhs-english 失败: $_" }
try { $r = opencli xiaohongshu search "跨文化沟通培训" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\xhs-crossculture.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ xhs-crossculture 失败: $_" }
try { $r = opencli xiaohongshu search "出海企业人才培养" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\xhs-talent.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ xhs-talent 失败: $_" }
try { $r = opencli xiaohongshu search "行业英语" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\xhs-industry-english.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ xhs-industry-english 失败: $_" }
try { $r = opencli xiaohongshu search "外派管理" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\xhs-expat.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ xhs-expat 失败: $_" }

# 微信公众号 (2个关键词，limit max 10)
try { $r = opencli weixin search "涉外培训" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\weixin-shewaipx.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ weixin-shewaipx 失败: $_" }
try { $r = opencli weixin search "跨文化沟通" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\weixin-crossculture.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ weixin-crossculture 失败: $_" }

# 知乎 (2个关键词，limit max 10)
try { $r = opencli zhihu search "企业出海培训" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\zhihu-chuhaipx.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ zhihu-chuhaipx 失败: $_" }
try { $r = opencli zhihu search "国际化人才培养" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\zhihu-talent.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ zhihu-talent 失败: $_" }

# 脉脉 (暂时跳过 - opencli 浏览器自动化问题)
# try { $r = opencli maimai search-talents "英语培训" --size 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\maimai-english.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ maimai-english 失败: $_" }
# try { $r = opencli maimai search-talents "跨文化管理" --size 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\maimai-crossculture.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ maimai-crossculture 失败: $_" }

# LinkedIn (暂时跳过 - opencli 页面结构变化)
# try { $r = opencli linkedin search "cross-cultural training" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\linkedin-crossculture.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ linkedin-crossculture 失败: $_" }
# try { $r = opencli linkedin search "global talent development" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\linkedin-talent.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ linkedin-talent 失败: $_" }

# 36氪 (3个关键词)
try { $r = opencli 36kr search "企业出海" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\36kr-chuahai.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ 36kr-chuahai 失败: $_" }
try { $r = opencli 36kr search "国际化人才" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\36kr-talent.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ 36kr-talent 失败: $_" }
try { $r = opencli 36kr search "属地化" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\36kr-localization.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ 36kr-localization 失败: $_" }

# B站 (4个关键词)
try { $r = opencli bilibili search "跨文化沟通" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\bili-crossculture.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ bili-crossculture 失败: $_" }
try { $r = opencli bilibili search "企业英语" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\bili-english.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ bili-english 失败: $_" }
try { $r = opencli bilibili search "商务英语" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\bili-bizenglish.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ bili-bizenglish 失败: $_" }
try { $r = opencli bilibili search "职场演讲" --limit 20 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\bili-speech.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ bili-speech 失败: $_" }

# 微博 (2个关键词，limit max 10)
try { $r = opencli weibo search "企业培训 出海" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\weibo-chuahai.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ weibo-chuahai 失败: $_" }
try { $r = opencli weibo search "跨文化" --limit 10 -f md 2>$null; if ($r) { [System.IO.File]::WriteAllText("$o\weibo-crossculture.md", $r, [System.Text.Encoding]::UTF8) } } catch { Write-Host "⚠ weibo-crossculture 失败: $_" }

Write-Host "✅ $d 采集完成 (6平台 x 18关键词)"
