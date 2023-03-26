import streamlit as st

st.set_page_config(page_title="Skylinemines Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('Hills', 'Desert', 'Mountains','Volcano','Seashore'))
st.subheader("Which Block")
if dim=="Hills":
     block = st.radio(
          "",
          ('Moss-Coal Mix', 'Coal-Copper Mix', 'Copper-Mosaic Mix','Hills Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Moss-Iron Mix':
          a = int(val / 64)
          b = val % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of T3 Moss and Coal")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Moss and Coal ")
     elif block=="Coal-Copper Mix":
          a=val*4
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Coal and Copper")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Coal and Copper ")
     elif block=="Copper-Mosaic Mix":
          a=val*8
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Copper and Mosaic")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Copper and Mosaic ")
     else:
          dia=val*36
          eme=val*24
          iron=val*12
          if ((iron % 64)==0):
               st.header(f"You need {int(iron / 64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(iron / 64):,d} Stacks and {iron % 64} T3 Coal")
          if ((dia % 64)==0):
               st.header(f"You need {int(dia / 64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(dia/64):,d} Stacks and {dia%64} T3 Copper")
          if ((eme % 64)==0):
               st.header(f"You need {int(eme / 64):,d} Stacks of T3 Mosaic")
          else:
               st.header(f"You need {int(eme / 64):,d} Stacks and {eme % 64} T3 Mosaic")
elif dim=="Desert":
     block = st.radio(
          "",
          ('Andesite-Granite Mix','Granite-Iron Mix','Iron-Forest Glass Mix','Desert Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Andesite-Granite Mix':
          a=val*2
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Andesite and Granite")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Andesite and Granite ")
     elif block == "Granite-Copper Mix":
          pri = val * 6
          fd=val*5
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Granite")
          else:
               st.header(f"You need {int(pri/64):,d} stacks and {pri%64} blocks of T3 Granite")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(fd/64):,d} stacks and {fd%64} blocks of T3 Iron")
     elif block == "Iron-Forest Glass Mix":
          a = val * 10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Iron and Forest Glass ")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Forest Glass ")
     else:
          ame = val * 24
          fd = val * 60
          pri = val * 40
          if ((ame % 64)==0):
               st.header(f"You need {int(ame/64):,d} Stacks of T3 Granite")
          else:
               st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Granite ")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Iron")
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Forest Glass")
          else:
               st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Forest Glass")
elif dim=="Mountains":
     block = st.radio(
          "",
          ('Sandstone-Prismarine Mix','Prismarine-Oceanstone Mix','Oceanstone-Seashine Mix','Port Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Sandstone-Prismarine Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Sandstone and Prismarine")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Sandstone and Prismarine ")
     elif block == "Oceanstone-Seashine Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 and Oceanstone and Seashine")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Oceanstone and Seashine ")
     elif block == "Prismarine-Oceanstone Mix":
          fg=val*8
          hr=val*6
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Prismarine ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Oceanstone")
     else:
          mg = val * 40
          fg = val * 90
          hr = val * 60
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Prismarine")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Oceanstone ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Seashine")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Seashine ")
elif dim=="Volcano":
     block = st.radio(
          "",
          ('Moss stone-Star Rock Mix','Star Rock-Aztec Relic Mix','Aztec Relic-Amethyst Mix','Empire Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Moss stone-Star Rock Mix':
          a=val*5
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Gold and Moss stone and Star Rock")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Moss stone and Star Rock ")
     elif block == "Aztec Relic-Amethyst Mix":
          a = val * 13
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Aztec Relic and Amethyst")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Aztec Relic and Amethyst ")
     elif block == "Star Rock-Aztec Relic Mix":
          fg=val*8
          hr=val*7
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Star Rock")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Star Rock ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Aztec Relic")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Aztec Relic")
     else:
          mg = val * 48
          fg = val * 120
          hr = val * 78
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Star Rock")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Star Rock")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Aztec Relic")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Aztec Relic ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Amethyst ")
elif dim=="Seashore":
     block = st.radio(
          "",
          ('Marble-Purpur Mix','Purpur-Magma Mix','Magma-Obsidian Mix','Citadel Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Marble-Purpur Mix':
          a=val*6
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Marble and Purpur")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Marble and Purpur ")
     elif block == "Purpur-Magma Mix":
          fg=val*10
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Purpur")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Purpur ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Magma")
     elif block == "Magma-Obsidian Mix":
          fg=val*15
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Magma ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian")
     else:
          mg = val * 80
          fg = val * 184
          hr = val * 64
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of Purpur")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Purpur")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Magma ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian ")
