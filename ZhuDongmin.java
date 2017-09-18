package string;

public class ZhuDongmin {
	
	private static String restOfLastData;				// 两条数据解析成一条新数据后，还剩余的数据
//	private static int restOfLastDataLength;			// 解析完成后还剩余的长度
	private static int finalUnCompleteRestOfLength;		// 解析未完成后最终剩余的长度，在这里必定大于 0
	private static String unCompleteData;				// 解析了两条数据依然未完成的字符串

	public static void main(String[] args) {
		String str1 = "S2160041401B170000E803E803FFFF000000000000000062";
		String str2 = "S2240041520000000000000000000000000000FFFF000000000000000000000000000000004A";
		String str3 = "S224004172000000000000000000000000000000000000000000000000000000000000000028";
		String str4 = "S2140041920000000000000000000000000000000018";
		String str5 = "S2240041A20000000000006449010098490100CC490100004A0100344A0100684A01009C4AEF";
		String str6 = "S2240041C20100D04A0100044B0100000000000000000000000000000000000000000000006C";
		String str7 = "S2100041E2000000000000000000000000CC";
		
		String str8 = "1B170000E803E803FFFF00000000000000000000000000000000000000000000F";
		
//		System.out.println(str8.length());
//		
//		System.out.println(calculateIntervalOfAddressCode(getAddressCode(str1),getAddressCode(str2)));
//		System.out.println(calculateIntervalOfAddressCode(getAddressCode(str2),getAddressCode(str3)));
//		System.out.println(calculateIntervalOfAddressCode(getAddressCode(str3),getAddressCode(str4)));
//		System.out.println(calculateIntervalOfAddressCode(getAddressCode(str4),getAddressCode(str5)));
//		System.out.println(calculateIntervalOfAddressCode(getAddressCode(str5),getAddressCode(str6)));
//		System.out.println(calculateIntervalOfAddressCode(getAddressCode(str6),getAddressCode(str7)));
		
		System.out.println(parse(str1,str2));
		System.out.println(parse(str3,str4));
		System.out.println(parse(str5,str6));
	}
	
	/**
	 * 获取每行的纯数据长度 = 数据长度 - 6（地址长度）-2（检验码长度）
	 * @param str
	 * @return
	 */
	public static int getDataLength(String str){
		String strDataLength = str.substring(2, 4);
		int dataLength = Integer.valueOf(strDataLength, 16) * 2;
		return dataLength - 8;
	}
	
	/**
	 * 获取纯数据
	 * @param str
	 * @return
	 */
	public static String getData(String str){
		String substringIncludeCheckCode = str.substring(10);
		int length = substringIncludeCheckCode.length();
		String data = substringIncludeCheckCode.substring(0, length-2);//去除校验码
		return data;
	}
	
	/**
	 * 获取地址码
	 * @param str
	 * @return
	 */
	public static String getAddressCode(String str){
		String address = str.substring(4, 10);
		return address;
	}
	
	/**
	 * 地址码相减
	 * @param addressCode1
	 * @param addressCode2
	 * @return
	 */
	public static int calculateIntervalOfAddressCode(String addressCode1,String addressCode2){
		int address1 = Integer.valueOf(addressCode1, 16);
		int address2 = Integer.valueOf(addressCode2, 16);
		return address2 - address1;
	}
	
	/**
	 * 按顺序来，一次性加入两条数据
	 * @param str
	 * @param str2
	 * @return
	 */
	public static String parse(String str,String str2){
		// 问题点：	1. 如果 restOfLastData 的数据长度已经够了，该怎么处理。
		//			2. 如果 str 和 str2 的数据长度都足够，该怎么处理。
		
		int restOfLastDataLength = 0;		// 上一次解析完成后还剩余的长度
		int restOfLength = 0;					// 64个数据位还剩余的位数 
		int dataLength = getDataLength(str);	// str 的有效数据长度
		// 这是第一条数据
		StringBuilder stringBuilder = new StringBuilder();
		if(unCompleteData != null){		// 有未完成的数据
			System.out.println("有未完成的数据的数据");
			stringBuilder.append(unCompleteData);
			restOfLength = 64 - unCompleteData.length() - dataLength;
			unCompleteData = null;
		}
		else		// 没有未完成的数据
		{
		System.out.println("没有未完成的数据");
		stringBuilder.append("24-").
					  append(getAddressCode(str)).	// 这个地址你想办法弄吧
					  append("-20-");
		if(restOfLastData != null){		// 如果还剩余未用完的数据
			stringBuilder.append(restOfLastData);
			restOfLastDataLength = restOfLastData.length();
			System.out.println("restOfLastData != null  restOfLastData : "+ restOfLastData +" length : "+ restOfLastDataLength);
			restOfLastData = null; 		// 用过了，所以置空
		}
		restOfLength = 64 - dataLength - restOfLastDataLength;		// 剩余 restOfLength 个数据填充
		}
		
		if(restOfLength < 0){							// 解析完成，还剩一点字符串，和str2
			System.out.println("restOfLastDataLength ："+ restOfLastDataLength +" getData(str) : "+getData(str)+"  dataLength : "+dataLength+"  restOfLength : "+restOfLength);
			String strAvalible = getData(str).substring(0, dataLength + restOfLength);
			stringBuilder.append(strAvalible);
			restOfLastData = getData(str2) + getData(str).substring(dataLength + restOfLength);
			unCompleteData = null;						// 解析完成，unCompleteData 置空
			return stringBuilder.toString();
		}else if(restOfLength == 0){					// 加上str刚好解析完，还剩 str2
			unCompleteData = null;						// 解析完成，unCompleteData 置空
			restOfLastData = getData(str2);
			return stringBuilder.toString();
		}
		
		stringBuilder.append(getData(str));
		
		
		String str2Data = getData(str2);
		if(str2Data.length() < restOfLength){	// 如果剩余的数据长度 都大于 str2 的长度，那就下一条
			System.out.println("str2Data.length() < restOfLength");
			stringBuilder.append(str2Data);
			finalUnCompleteRestOfLength = restOfLength - str2Data.length();	//解析未完成后最终剩余的长度，在这里必定大于 0
			unCompleteData = stringBuilder.toString();				//解析了两条数据依然未完成的字符串
			return "";									// 如果解析未完成，返回空字符""。
		}else if(str2Data.length() == restOfLength){	// 如果刚好等于
			System.out.println("str2Data.length() == restOfLength");
			stringBuilder.append(str2Data);
			unCompleteData = null;						// 解析完成，unCompleteData 置空
			return stringBuilder.toString();
		}else{									// 如果剩余数据长度 小于 str2 的长度，剩余的字符串可以保留着下一条数据
			System.out.println("str2Data.length() > restOfLength  restOfLength : "+ restOfLength);
			String str2AvaliableData = str2Data.substring(0, restOfLength);//包头不包尾
			stringBuilder.append(str2AvaliableData);
			restOfLastData = str2Data.substring(restOfLength);		
			unCompleteData = null;						// 解析完成，unCompleteData 置空
			return stringBuilder.toString();
		}
	}
}
