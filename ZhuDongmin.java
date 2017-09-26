package string;

public class ZhuDongmin {
	
	private static String restOfLastData;				// 两条数据解析成一条新数据后，还剩余的数据
	private static boolean hasFinishedParseData;
	private static boolean isFirstTimeToParse = true;	// 是否解析第一条数据
	private static String addressCode;

	public static void main(String[] args) {
		String str1 = "S2160041401B170000E803E803FFFF000000000000000062";	// 末尾16个0 ， 20个数字
		String str2 = "S2240041520000000000000000000000000000FFFF000000000000000000000000000000004A";
		String str3 = "S224004172000000000000000000000000000000000000000000000000000000000000000028";
		String str4 = "S2140041920000000000000000000000000000000018";
		String str5 = "S2240041A20000000000006449010098490100CC490100004A0100344A0100684A01009C4AEF";
		String str6 = "S2240041C20100D04A0100044B0100000000000000000000000000000000000000000000006C";
		String str7 = "S2100041E2000000000000000000000000CC";
		
		String str8 = "A30CF4A3FEF47FFEF3FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF";
		
		String str9  = "S20D00C1A0A30CF4A3FEF47FFEF3E9";
		String str10 = "S22400C1CCB7A50CB7A40CD90FA70CD90FA90CB7A30C0BA30CB3778026007DCA0D33A30CD849";
		String str11 = "S22400C1EC0CAF0CA7A30CFEEA0BA60CB3D1206E127EBF230B6AFBD812F54B037E8F2B0BFE0A";
		Integer valueOf = Integer.valueOf("00C1A0", 16);
		System.out.println(toHexString(valueOf));
//		
//		try{
//		System.out.println(parse(str1));
//		System.out.println(parse(str2));
//		System.out.println(parse(str3));
//		System.out.println(parse(str4));
//		System.out.println(parse(str5));
//		System.out.println(parse(str6));
//		}catch (Exception e){
//			e.printStackTrace();
//		}
		
		try {
			System.out.println(parse(str9));
			System.out.println(parse(str10));
			System.out.println(parse(str11));
		} catch (Exception e) {
			e.printStackTrace();
		}
		
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
	 * @throws Exception 
	 */
	public static String getData(String str) throws Exception{
		if(str.startsWith("S2")){	// 以 S2 开头的数据 才能这样操作，还有其他什么条件
			String substringIncludeCheckCode = str.substring(10);
			int length = substringIncludeCheckCode.length();
			String data = substringIncludeCheckCode.substring(0, length-2);//去除校验码
			return data;
		}else{						// 否则抛出异常
			throw new Exception("解析的数据不是以 S2 开头");
		}
	}
	
	/**
	 * 获取以 24 开头的纯数据
	 * @param str
	 * @return
	 */
	public static String get24Data(String str) throws Exception{
		if(str.startsWith("24-")){
			String data = str.substring(13);
			return data;
		}else{
			throw new Exception("解析的数据不是以 24 开头");
		}
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
	
	
	public static String parse(String str) throws Exception{
		
		StringBuilder stringBuilder = new StringBuilder();
		int dataLength = getDataLength(str);
		String data = getData(str);
		int restOfLastDataLength = 0 ;
		if(isFirstTimeToParse){
			addressCode = getAddressCode(str);
		}
		String addressCode2 = getAddressCode(str);
		int addressInterval = calculateIntervalOfAddressCode(addressCode, addressCode2);
		if( addressInterval > 0x20 ){		// 如果前一个地址与后一个地址的间隔大于 0x20 
			// 补充的 F 的个数为原来起始地址的 - 原来起始地址 & 0x00001F
			int numOfF = Integer.valueOf(addressCode,16) - ( Integer.valueOf(addressCode,16) & 0xFFFFE0 );
			System.out.println("numOfF : "+numOfF);
			System.out.println("interval : "+ restOfLastData);
			StringBuilder sBuilder = new StringBuilder(restOfLastData);
			for(int i = 0; i < 64 - get24Data(restOfLastData).length() ; i++ ){
				sBuilder.append("f");
			}
			addressCode += 0x20;
			return sBuilder.toString();
			
		}
		
		
		if(hasFinishedParseData || isFirstTimeToParse){	// 如果已经解析成功了一条数据
			System.out.println("hasFinishedParseData or isFirstTimeToParse");
			isFirstTimeToParse = false;
			stringBuilder.append("24-").
						  append(addressCode).	// 这个地址你想办法弄吧，在 下面的 return 前面，如果不是 return "",地址就加 20。
						  append("-20-");
			if(restOfLastData != null){			// restOfLastData 包含纯数据		
				stringBuilder.append(restOfLastData);
				restOfLastDataLength = restOfLastData.length();
			}
		}else{
			// hasFinishedParseData 为 false 的时候 restOfLastData 一定不为空。
			System.out.println("None of hasFinishedParseData , isFirstTimeToParse");
			stringBuilder.append(restOfLastData);	// restOfLastData 包含 24-……
			restOfLastData = get24Data(restOfLastData);	// 获取纯数据
			restOfLastDataLength = restOfLastData.length();
		}
		
		// 凑够64位数据的 剩余的数据 = 64 - 传进来的字符串的长度 - 上一次剩余的字符串的长度（第一次为 0 ）
		int restOfDataLength = 64 - dataLength - restOfLastDataLength ;	
		System.out.println("restOfDataLength : "+restOfDataLength+"  dataLength : "+dataLength+"  restOfLastDataLength : "+restOfLastDataLength);
		
		if(restOfDataLength > 0){		// 还不够 64 个数据位
			restOfLastData = stringBuilder.append(data).toString();
			System.out.println("未解析完成，有数据 ： "+ restOfLastData);
			hasFinishedParseData = false;	// 还未解析成功一条数据
			return "未解析完成";
		}else if(restOfDataLength == 0){	// 刚好够 64 个数据位
			restOfLastData = null;
			hasFinishedParseData = true;	// 已经解析成功了一条数据
			System.out.println("刚好解析完成");
			addressCode += 0x20;		// addressCode2 已经变为了下一条地址的上一条地址
			return stringBuilder.append(data).toString();
		}else{							// 超出了 64 个数据位
			String avaliableData = data.substring(0, data.length() + restOfDataLength);// 这部分数据可凑够64个
			restOfLastData = data.substring(data.length() + restOfDataLength);			// 这部分是剩余的数据
			System.out.println("data : "+data+"  avaliableData : "+avaliableData+"  restOfLastData : "+restOfLastData);
			hasFinishedParseData = true;	// 已经解析成功了一条数据
			addressCode += 0x20;		// addressCode2 已经变为了下一条地址的上一条地址
			System.out.println("解析完成，并且还剩下  "+ restOfLastData);
			return stringBuilder.append(avaliableData).toString();
		}
		
	}
	
//	/**
//	 * 按顺序来，一次性加入两条数据
//	 * @param str
//	 * @param str2
//	 * @return
//	 */
//	public static String parse(String str,String str2){
//		// 问题点：	1. 如果 restOfLastData 的数据长度已经够了，该怎么处理。
//		//			2. 如果 str 和 str2 的数据长度都足够，该怎么处理。
//		
//		int restOfLastDataLength = 0;		// 上一次解析完成后还剩余的长度
//		int restOfLength = 0;					// 64个数据位还剩余的位数 
//		int dataLength = getDataLength(str);	// str 的有效数据长度
//		// 这是第一条数据
//		StringBuilder stringBuilder = new StringBuilder();
//		if(unCompleteData != null){		// 有未完成的数据
//			System.out.println("有未完成的数据的数据");
//			stringBuilder.append(unCompleteData);
//			restOfLength = 64 - unCompleteData.length() - dataLength;
//			unCompleteData = null;
//		}
//		else		// 没有未完成的数据
//		{
//		System.out.println("没有未完成的数据");
//		stringBuilder.append("24-").
//					  append(getAddressCode(str)).	// 这个地址你想办法弄吧
//					  append("-20-");
//		if(restOfLastData != null){		// 如果还剩余未用完的数据
//			stringBuilder.append(restOfLastData);
//			restOfLastDataLength = restOfLastData.length();
//			System.out.println("restOfLastData != null  restOfLastData : "+ restOfLastData +" length : "+ restOfLastDataLength);
//			restOfLastData = null; 		// 用过了，所以置空
//		}
//		restOfLength = 64 - dataLength - restOfLastDataLength;		// 剩余 restOfLength 个数据填充
//		}
//		
//		if(restOfLength < 0){							// 解析完成，还剩一点字符串，和str2
//			System.out.println("restOfLastDataLength ："+ restOfLastDataLength +" getData(str) : "+getData(str)+"  dataLength : "+dataLength+"  restOfLength : "+restOfLength);
//			String strAvalible = getData(str).substring(0, dataLength + restOfLength);
//			stringBuilder.append(strAvalible);
//			restOfLastData = getData(str2) + getData(str).substring(dataLength + restOfLength);
//			unCompleteData = null;						// 解析完成，unCompleteData 置空
//			return stringBuilder.toString();
//		}else if(restOfLength == 0){					// 加上str刚好解析完，还剩 str2
//			unCompleteData = null;						// 解析完成，unCompleteData 置空
//			restOfLastData = getData(str2);
//			return stringBuilder.toString();
//		}
//		
//		stringBuilder.append(getData(str));
//		
//		
//		String str2Data = getData(str2);
//		if(str2Data.length() < restOfLength){	// 如果剩余的数据长度 都大于 str2 的长度，那就下一条
//			System.out.println("str2Data.length() < restOfLength");
//			stringBuilder.append(str2Data);
//			finalUnCompleteRestOfLength = restOfLength - str2Data.length();	//解析未完成后最终剩余的长度，在这里必定大于 0
//			unCompleteData = stringBuilder.toString();				//解析了两条数据依然未完成的字符串
//			return "";									// 如果解析未完成，返回空字符""。
//		}else if(str2Data.length() == restOfLength){	// 如果刚好等于
//			System.out.println("str2Data.length() == restOfLength");
//			stringBuilder.append(str2Data);
//			unCompleteData = null;						// 解析完成，unCompleteData 置空
//			return stringBuilder.toString();
//		}else{									// 如果剩余数据长度 小于 str2 的长度，剩余的字符串可以保留着下一条数据
//			System.out.println("str2Data.length() > restOfLength  restOfLength : "+ restOfLength);
//			String str2AvaliableData = str2Data.substring(0, restOfLength);//包头不包尾
//			stringBuilder.append(str2AvaliableData);
//			restOfLastData = str2Data.substring(restOfLength);		
//			unCompleteData = null;						// 解析完成，unCompleteData 置空
//			return stringBuilder.toString();
//		}
//	}
	public static String toHexString(int i) {
		String value = Integer.toHexString(i);
		int length = value.length();
		int lengthOfZero = 6 - length;
		for( int j= 0; j < lengthOfZero; j++)
			value = "0" + value;
		return value;
	}
	
}
