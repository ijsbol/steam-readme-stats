# Steam Readme Stats
 Embed your steam stats into your readme

![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/playtime?format=total_days&style=for-the-badge)
![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/playtime?format=total_hours&style=for-the-badge)
![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/playtime?format=total_minutes&style=for-the-badge)
![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/playtime?format=days_and_hours&style=for-the-badge)
![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/playtime?format=hours_and_minutes&style=for-the-badge)
![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/playtime?format=full&style=for-the-badge)
![img](https://steam-readme-stats.uwu.gal/api/76561198242540404/stats/badge/games?style=for-the-badge)


## How to use
Copy paste the following into your readme
```
![img](https://steam-readme-stats.uwu.gal/api/YOUR_STEAM_USERID_HERE/stats/badge/playtime?format=total_days)
```
Where `YOUR_STEAM_ID_HERE` is replaced with your SteamID64 (Dec), which can be found here: https://www.steamidfinder.com


## Documentation
### `/api/:steamid_64/stats/badge/playtime`
|Accepted query parameters|Values|
| -- | -- |
| label | any string |
| color | hex, rgb, rgba, hsl, hsla and css named colors supported |
| format | `total_days`, `total_hours`, `total_minutes`, `days_and_hours`, `hours_and_minutes`, `full` |
| label_color | hex, rgb, rgba, hsl, hsla and css named colors supported |
| style | `flat`, `flat-square`, `for-the-badge`, `plastic`, `social` |

### `/api/:steamid_64/stats/badge/games`
|Accepted query parameters|Values|
| -- | -- |
| label | any string |
| color | hex, rgb, rgba, hsl, hsla and css named colors supported |
| label_color | hex, rgb, rgba, hsl, hsla and css named colors supported |
| style | `flat`, `flat-square`, `for-the-badge`, `plastic`, `social` |
